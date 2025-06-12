#!/usr/bin/env python3
"""
Godot-Jenova Engine Cleanup Script (Darwin ARM64)
Removes non-Darwin platforms and build artifacts to prepare for GitHub upload.
Optimized for Darwin ARM64 development only.
"""

import os
import shutil
import fnmatch
import argparse
from pathlib import Path

class EngineModCleanup:
	def __init__(self, mod_path):
		self.mod_path = Path(mod_path).resolve()
		self.files_to_remove = []
		self.dirs_to_remove = []
		self.total_size_saved = 0
		self.size_threshold = 100 * 1024 * 1024  # 100MB default threshold
		
		# Large file extensions to remove
		self.large_file_extensions = {
			# Binary/executable files
			'.exe', '.dll', '.so', '.dylib', '.app', '.pkg', '.dmg',
			# Archive files
			'.zip', '.tar', '.gz', '.7z', '.rar', '.bz2', '.xz',
			# Media files
			'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv',
			'.mp3', '.wav', '.flac', '.ogg', '.m4a',
			'.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.psd',
			# 3D model files
			'.fbx', '.obj', '.dae', '.3ds', '.blend', '.max', '.maya',
			# Engine-specific large files
			'.uasset', '.umap',  # Unreal
			'.unity', '.asset',  # Unity
			'.godot', '.scn', '.tscn', '.res', '.tres',  # Godot (some can be large)
			# Development files
			'.iso', '.img', '.vdi', '.vmdk',
			# Database files
			'.db', '.sqlite', '.mdb',
			# Log files (can get very large)
			'.log',
		}
		
		# Godot-specific large directories to remove
		self.large_directories = {
			# Build outputs (this is 8.6GB!)
			'bin', 'bin/obj',
			# Platform directories to remove (keep only macos)
			'platform/android', 'platform/ios', 'platform/linuxbsd', 
			'platform/visionos', 'platform/web', 'platform/windows',
			# General build outputs
			'build', 'Build', 'BUILD', 'builds', 'Builds',
			'obj', 'Obj', 'OBJ', 'out', 'Out', 'OUTPUT',
			# Debug/Release builds  
			'Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel',
			# IDE/Editor generated
			'.vs', '.vscode/ipch', '.idea', 'DerivedData',
			# Python cache
			'__pycache__',
			# Package managers
			'node_modules', 'target',
			# Godot-specific cache
			'.import', '.godot', '.tmp',
			# Version control
			'.svn', '.hg', '.bzr',
			# Cache directories
			'cache', 'Cache', 'CACHE', 'tmp', 'temp', 'Temp', 'TMP',
		}
		
		# Godot-specific modules that are platform-specific and can be removed
		self.removable_modules = {
			# Platform-specific modules
			'modules/mono',  # C# support (if not needed)
			'modules/webrtc', 'modules/webxr',  # Web-specific
			'modules/mobile_vr',  # Mobile VR
			# Graphics APIs not needed on macOS
			'modules/vulkan',  # If using Metal instead
			'modules/d3d12',   # DirectX (Windows only)
		}
		
		# Platform-specific thirdparty libraries to clean up
		self.thirdparty_cleanup = {
			# Windows-specific
			'thirdparty/d3d12ma', 'thirdparty/directx_headers',
			# Web-specific  
			'thirdparty/embree/kernels/subdiv/bezier_curve.h',
			# Android-specific
			'thirdparty/vulkan/registry',
		}
		
		# Platform-specific files to remove (keeping only Darwin ARM64)
		self.platform_specific_extensions = {
			# Windows
			'.exe', '.dll', '.lib', '.pdb', '.ilk', '.exp', '.manifest',
			# Linux  
			'.so', '.a',
			# Web
			'.wasm', '.js', '.html',
			# Android
			'.apk', '.aab', '.jar',
			# iOS (but keep some that might be needed)
			'.ipa',
		}
		
		# Godot engine-specific files to keep
		self.keep_extensions = {
			'.cpp', '.hpp', '.h', '.c', '.cc', '.cxx',
			'.cs', '.py', '.js', '.ts', '.gd', '.lua',
			'.json', '.xml', '.yaml', '.yml', '.toml', '.ini', '.cfg',
			'.md', '.txt', '.rst',
			'.cmake', '.make', '.makefile',
			'.sh', '.bat', '.ps1',
			'.gitignore', '.gitattributes', '.gitmodules',
			# Godot-specific
			'.godot', '.tscn', '.scn', '.tres', '.res',
			'.import', '.remap', '.depmap',
			# Build system
			'.py', '.scons', '.scu',
		}
		
		# Patterns to always keep
		self.keep_patterns = [
			'README*', 'LICENSE*', 'CHANGELOG*', 'CONTRIBUTING*',
			'*.Builder*', 'CMakeLists.txt', 'Makefile*',
			'package.json', 'Cargo.toml', 'requirements.txt',
		]

	def should_keep_file(self, file_path):
		"""Determine if a file should be kept."""
		file_name = file_path.name
		file_ext = file_path.suffix.lower()
		file_size = self.get_file_size(file_path)
		rel_path = str(file_path.relative_to(self.mod_path)).lower()
		
		# Always keep files matching keep patterns
		for pattern in self.keep_patterns:
			if fnmatch.fnmatch(file_name, pattern):
				return True
		
		# Always keep source code and config files
		if file_ext in self.keep_extensions:
			return True
			
		# Remove platform-specific files for non-Darwin platforms
		if file_ext in self.platform_specific_extensions:
			# Keep .dylib files (Darwin libraries)
			if file_ext == '.dylib':
				return True
			return False
			
		# Remove platform-specific directories in path
		platform_keywords = ['win32', 'windows', 'linux', 'android', 'web', 'javascript']
		if any(keyword in rel_path for keyword in platform_keywords):
			return False
			
		# Remove large file types
		if file_ext in self.large_file_extensions:
			return False
			
		# Remove files over size threshold (except source code)
		if file_size > self.size_threshold:
			print(f"⚠️  Large file detected: {file_path.relative_to(self.mod_path)} ({self.format_size(file_size)})")
			return False
			
		# Keep smaller files by default
		return True

	def should_keep_dir(self, dir_path):
		"""Determine if a directory should be kept."""
		dir_name = dir_path.name
		rel_path = str(dir_path.relative_to(self.mod_path))
		
		# Remove the massive bin directory (8.6GB of build artifacts)
		if rel_path == 'bin':
			return False
			
		# Keep only Darwin ARM64 platform, remove all others
		if rel_path.startswith('platform/') and dir_name != 'macos':
			if dir_name in ['android', 'ios', 'linuxbsd', 'visionos', 'web', 'windows']:
				print(f"  🗑️  Removing non-Darwin platform: {rel_path}")
				return False
		
		# Remove specific modules we don't need
		if rel_path in self.removable_modules:
			return False
			
		# Remove known large directories
		if dir_name in self.large_directories or rel_path in self.large_directories:
			return False
			
		# Remove thirdparty subdirectories we don't need
		if rel_path in self.thirdparty_cleanup:
			return False
			
		# Keep source directories
		source_dirs = {'src', 'source', 'Source', 'core', 'scene', 'servers', 'editor', 'main'}
		if dir_name in source_dirs:
			return True
			
		# Keep other directories by default
		return True

	def get_file_size(self, file_path):
		"""Get file size in bytes."""
		try:
			return file_path.stat().st_size
		except (OSError, FileNotFoundError):
			return 0

	def format_size(self, size_bytes):
		"""Format file size in human readable format."""
		for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
			if size_bytes < 1024.0:
				return f"{size_bytes:.1f} {unit}"
			size_bytes /= 1024.0
		return f"{size_bytes:.1f} PB"

	def scan_mod_directory(self):
		"""Scan engine mod directory and identify large files to remove."""
		print(f"Scanning engine mod: {self.mod_path}")
		
		large_files = []
		
		for root, dirs, files in os.walk(self.mod_path):
			root_path = Path(root)
			
			# Skip .git directory
			if '.git' in root_path.parts:
				continue
				
			# Check directories
			dirs_to_remove_from_walk = []
			for dir_name in dirs[:]:
				dir_path = root_path / dir_name
				if not self.should_keep_dir(dir_path):
					self.dirs_to_remove.append(dir_path)
					dirs_to_remove_from_walk.append(dir_name)
					
			# Remove directories from walk
			for dir_name in dirs_to_remove_from_walk:
				dirs.remove(dir_name)
			
			# Check files
			for file_name in files:
				file_path = root_path / file_name
				file_size = self.get_file_size(file_path)
				
				if not self.should_keep_file(file_path):
					self.files_to_remove.append((file_path, file_size))
					self.total_size_saved += file_size
				elif file_size > 10 * 1024 * 1024:  # Note files over 10MB
					large_files.append((file_path, file_size))
		
		return large_files

	def preview_cleanup(self):
		"""Show what will be removed."""
		print("\n" + "="*70)
		print("GODOT-JENOVA DARWIN ARM64 CLEANUP PREVIEW")
		print("="*70)
		print("🍎 Keeping: platform/macos (Darwin ARM64 target)")
		print("🗑️  Removing: All other platforms (Windows, Linux, Android, etc.)")
		
		if self.dirs_to_remove:
			print(f"\nDirectories to remove ({len(self.dirs_to_remove)}):")
			for dir_path in sorted(self.dirs_to_remove):
				rel_path = dir_path.relative_to(self.mod_path)
				print(f"  📁 {rel_path}")
		
		if self.files_to_remove:
			print(f"\nFiles to remove ({len(self.files_to_remove)}):")
			for file_path, size in sorted(self.files_to_remove, key=lambda x: x[1], reverse=True):
				rel_path = file_path.relative_to(self.mod_path)
				print(f"  📄 {rel_path} ({self.format_size(size)})")
		
		print(f"\nTotal space to be freed: {self.format_size(self.total_size_saved)}")

	def show_large_files_kept(self, large_files):
		"""Show large files that will be kept."""
		if large_files:
			print(f"\nLarge files being kept ({len(large_files)}):")
			for file_path, size in sorted(large_files, key=lambda x: x[1], reverse=True):
				rel_path = file_path.relative_to(self.mod_path)
				print(f"  ⚠️  {rel_path} ({self.format_size(size)})")
			print("\nConsider if these files are necessary for GitHub.")

	def execute_cleanup(self, dry_run=True):
		"""Execute the cleanup operation."""
		if dry_run:
			print("\n🔍 DRY RUN - No files will actually be deleted")
			return
		
		print("\n🗑️  EXECUTING CLEANUP...")
		
		removed_files = 0
		removed_dirs = 0
		actual_size_saved = 0
		
		# Remove files
		for file_path, estimated_size in self.files_to_remove:
			try:
				if file_path.exists():
					actual_size = self.get_file_size(file_path)
					file_path.unlink()
					removed_files += 1
					actual_size_saved += actual_size
					print(f"  ✅ Removed: {file_path.relative_to(self.mod_path)}")
			except Exception as e:
				print(f"  ❌ Error removing {file_path.relative_to(self.mod_path)}: {e}")
		
		# Remove directories
		for dir_path in self.dirs_to_remove:
			try:
				if dir_path.exists():
					shutil.rmtree(dir_path)
					removed_dirs += 1
					print(f"  ✅ Removed directory: {dir_path.relative_to(self.mod_path)}")
			except Exception as e:
				print(f"  ❌ Error removing {dir_path.relative_to(self.mod_path)}: {e}")
		
		print(f"\n✨ Engine mod cleanup complete!")
		print(f"   📄 Files removed: {removed_files}")
		print(f"   📁 Directories removed: {removed_dirs}")
		print(f"   💾 Space freed: {self.format_size(actual_size_saved)}")

def main():
	parser = argparse.ArgumentParser(
		description="Clean up engine mod by removing large files for GitHub upload"
	)
	parser.add_argument(
		"mod_path", 
		nargs="?", 
		default=".", 
		help="Path to engine mod directory (default: current directory)"
	)
	parser.add_argument(
		"--execute", 
		action="store_true", 
		help="Actually remove files (default is dry-run)"
	)
	parser.add_argument(
		"--threshold", 
		type=int, 
		default=100, 
		help="Size threshold in MB for large files (default: 100MB)"
	)
	parser.add_argument(
		"--force", 
		action="store_true", 
		help="Skip confirmation prompt"
	)
	
	args = parser.parse_args()
	
	# Validate mod path
	mod_path = Path(args.mod_path).resolve()
	if not mod_path.exists():
		print(f"❌ Error: Engine mod path does not exist: {mod_path}")
		return 1
	
	# Initialize cleanup
	cleanup = EngineModCleanup(mod_path)
	cleanup.size_threshold = args.threshold * 1024 * 1024  # Convert MB to bytes
	
	# Scan mod directory
	large_files = cleanup.scan_mod_directory()
	
	# Show preview
	cleanup.preview_cleanup()
	cleanup.show_large_files_kept(large_files)
	
	# Execute cleanup
	if args.execute:
		if not args.force:
			print(f"\n⚠️  This will permanently delete {len(cleanup.files_to_remove)} files and {len(cleanup.dirs_to_remove)} directories!")
			response = input("Are you sure you want to continue? (y/N): ")
			if response.lower() != 'y':
				print("Cleanup cancelled.")
				return 0
		
		cleanup.execute_cleanup(dry_run=False)
	else:
		print(f"\n💡 This was a dry run. Use --execute to actually remove files.")
		print(f"💡 Example: python {parser.prog} {args.mod_path} --execute")
	
	return 0

if __name__ == "__main__":
	exit(main())