# Godot Engine

<p align="center">
  <a href="https://godotengine.org">
    <img src="logo_outlined.svg" width="400" alt="Godot Engine logo">
  </a>
</p>


![Screenshot of a 3D scene in the Godot Engine editor](https://raw.githubusercontent.com/lithalean/GameEngine/main/docs/screenshots/editor_jenova_demo_1920x1080.jpg)


```
┌─────────────────────────────────────────┐
│           SwiftUI Native Layer          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐    │
│  │ Splash  │ │  Menu   │ │Settings │    │
│  └─────────┘ └─────────┘ └─────────┘    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐    │
│  │ Social  │ │   IAP   │ │Profile  │    │
│  └─────────┘ └─────────┘ └─────────┘    │
└─────────────────────────────────────────┘
                    ↕ Bridge
┌─────────────────────────────────────────┐
│        Godot + Jenova Core              │
│   ┌─────────────────────────────────┐   │
│   │    Pure Gameplay Experience     │   │
│   │  • Game mechanics               │   │
│   │  • Physics & rendering          │   │
│   │  • Audio & effects              │   │
│   │  • Performance-critical C++     │   │
│   └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

# GameEngine Roadmap

## Project Overview
Darwin ARM64-only fork of the Jenova-compatible Godot engine that includes engine-level modifications to support the Jenova C++ scripting framework and hot-reloading capabilities.

## Current Status
- [x] **Base Godot engine** (forked from upstream)
- [x] **Jenova compatibility hooks** (integrated from TheAenema/godot-jenova)
- [x] **XCFramework building** (for other projects)
- [ ] **Darwin ARM64 optimization** 
- [ ] **Platform cleanup** (remove non-Darwin code)

## Core Components

### 1. Engine Core Modifications
- [ ] **Jenova Script Backend Integration**
  - [ ] C++ script class registration
  - [ ] Script instance management
  - [ ] Method binding interfaces
  - [ ] Property exposure system
- [ ] **Hot-Reload System (Sakura)**
  - [ ] Script change detection hooks
  - [ ] Safe module unloading
  - [ ] State preservation during reload
  - [ ] Editor integration for hot-reload
- [ ] **ClassDB Enhancements**
  - [ ] API type override methods
  - [ ] Dynamic class registration
  - [ ] Nested extension support
  - [ ] Runtime binding management

### 2. Editor Integration
- [ ] **C++ Script Support**
  - [ ] Syntax highlighting for C++ scripts
  - [ ] IntelliSense/code completion
  - [ ] Error reporting integration
  - [ ] Script template system
- [ ] **Development Tools**
  - [ ] Real-time compilation feedback
  - [ ] Debug integration for C++ scripts
  - [ ] Performance profiling hooks
  - [ ] Script dependency management
- [ ] **Asset Management**
  - [ ] C++ script asset handling
  - [ ] Automatic compilation triggers
  - [ ] Build output management
  - [ ] Library dependency tracking

### 3. Platform Optimization (Darwin ARM64)
- [ ] **Remove Non-Darwin Code**
  - [ ] Windows-specific implementations
  - [ ] Linux-specific code paths
  - [ ] Android/iOS simulator code
  - [ ] Web/WASM export functionality
- [ ] **Darwin-Specific Optimizations**
  - [ ] Apple Silicon performance tuning
  - [ ] Metal rendering optimizations
  - [ ] macOS-native file operations
  - [ ] Accelerate framework integration
- [ ] **Build System Cleanup**
  - [ ] Remove cross-platform build configs
  - [ ] Optimize for Xcode/clang only
  - [ ] Streamline dependency management
  - [ ] XCFramework generation improvements

### 4. EngineRuntime Integration
- [ ] **Runtime Loading**
  - [ ] Dynamic Runtime loading
  - [ ] Version compatibility checking
  - [ ] Graceful fallback mechanisms
  - [ ] Error handling and reporting
- [ ] **Communication Interface**
  - [ ] Engine-to-runtime messaging
  - [ ] Script compilation requests
  - [ ] Hot-reload notifications
  - [ ] Debug information exchange
- [ ] **Memory Management**
  - [ ] Shared memory pools
  - [ ] Garbage collection integration
  - [ ] Resource lifecycle management
  - [ ] Memory leak prevention

### 5. Performance & Stability
- [ ] **Performance Monitoring**
  - [ ] C++ script execution profiling
  - [ ] Hot-reload performance metrics
  - [ ] Memory usage tracking
  - [ ] Compilation time optimization
- [ ] **Stability Improvements**
  - [ ] Crash recovery mechanisms
  - [ ] Safe script isolation
  - [ ] Resource cleanup on errors
  - [ ] Thread safety enhancements
- [ ] **Testing Framework**
  - [ ] Automated C++ script testing
  - [ ] Hot-reload stress testing
  - [ ] Performance regression testing
  - [ ] Platform-specific test suites

### 6. Documentation & Examples
- [ ] **Developer Documentation**
  - [ ] Engine modification guidelines
  - [ ] API reference documentation
  - [ ] Hot-reload implementation details
  - [ ] Platform-specific build instructions
- [ ] **Example Projects**
  - [ ] Basic C++ scripting examples
  - [ ] Hot-reload demonstration
  - [ ] Performance comparison demos
  - [ ] Integration test projects
- [ ] **Migration Guides**
  - [ ] From standard Godot to Jenova
  - [ ] Cross-platform to Darwin ARM64
  - [ ] Build system migration
  - [ ] Deployment strategies

## Implementation Phases

### Phase 1: Platform Cleanup
- [ ] Remove Windows/Linux/Web platform code
- [ ] Clean up build system for Darwin ARM64 only
- [ ] Optimize for Apple Silicon performance
- [ ] Test basic engine functionality

### Phase 2: Core Jenova Integration
- [ ] Verify and enhance existing Jenova hooks
- [ ] Implement missing C++ script backend features
- [ ] Ensure hot-reload system works correctly
- [ ] Integrate with Jenova Runtime properly

### Phase 3: Editor Tools
- [ ] Enhance C++ script editing experience
- [ ] Implement real-time compilation feedback
- [ ] Add debugging and profiling tools
- [ ] Create script templates and examples

### Phase 4: Performance & Polish
- [ ] Optimize for Darwin ARM64 specifically
- [ ] Performance testing and tuning
- [ ] Stability improvements and bug fixes
- [ ] Documentation and examples

## Success Metrics
- [ ] **Build Size**: Reduce engine size by 60%+ (remove unused platforms)
- [ ] **Performance**: 15%+ improvement on Darwin ARM64 vs standard Godot
- [ ] **Hot-Reload**: Sub-second C++ script hot-reload times
- [ ] **Stability**: Zero crashes during normal C++ scripting workflow
- [ ] **XCFramework**: Reliable framework generation for other projects

## Dependencies
- **Jenova Runtime**: Must be compatible with engine modifications
- **Darwin SDK**: macOS/Xcode development tools
- **LLVM/Clang**: For C++ compilation and tooling
- **Ninja/CMake**: For build system optimization

## Notes
- **Target Platform**: Darwin ARM64 only (no cross-platform support)
- **Focus**: C++ scripting performance and developer experience
- **Integration**: Must work seamlessly with Jenova Runtime
- **Build Output**: XCFramework for integration with other projects