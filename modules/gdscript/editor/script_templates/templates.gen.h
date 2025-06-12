/**************************************************************************/
/*  templates.gen.h                                                       */
/**************************************************************************/
/*                         This file is part of:                          */
/*                             GODOT ENGINE                               */
/*                        https://godotengine.org                         */
/**************************************************************************/
/* Copyright (c) 2014-present Godot Engine contributors (see AUTHORS.md). */
/* Copyright (c) 2007-2014 Juan Linietsky, Ariel Manzur.                  */
/*                                                                        */
/* Permission is hereby granted, free of charge, to any person obtaining  */
/* a copy of this software and associated documentation files (the        */
/* "Software"), to deal in the Software without restriction, including    */
/* without limitation the rights to use, copy, modify, merge, publish,    */
/* distribute, sublicense, and/or sell copies of the Software, and to     */
/* permit persons to whom the Software is furnished to do so, subject to  */
/* the following conditions:                                              */
/*                                                                        */
/* The above copyright notice and this permission notice shall be         */
/* included in all copies or substantial portions of the Software.        */
/*                                                                        */
/* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,        */
/* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF     */
/* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. */
/* IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY   */
/* CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,   */
/* TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE      */
/* SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                 */
/**************************************************************************/

/* THIS FILE IS GENERATED. EDITS WILL BE LOST. */

#pragma once

#include "core/object/object.h"
#include "core/object/script_language.h"

inline constexpr int TEMPLATES_ARRAY_SIZE = 10;
static const struct ScriptLanguage::ScriptTemplate TEMPLATES[TEMPLATES_ARRAY_SIZE] = {
	{ String("CharacterBody2D"), String("Basic Movement"), String("Classic movement for gravity games (platformer, ...)"), String("extends _BASE_\n\n\nconst SPEED = 300.0\nconst JUMP_VELOCITY = -400.0\n\n\nfunc _physics_process(delta: float) -> void:\n_TS_# Add the gravity.\n_TS_if not is_on_floor():\n_TS__TS_velocity += get_gravity() * delta\n\n_TS_# Handle jump.\n_TS_if Input.is_action_just_pressed(\"ui_accept\") and is_on_floor():\n_TS__TS_velocity.y = JUMP_VELOCITY\n\n_TS_# Get the input direction and handle the movement/deceleration.\n_TS_# As good practice, you should replace UI actions with custom gameplay actions.\n_TS_var direction := Input.get_axis(\"ui_left\", \"ui_right\")\n_TS_if direction:\n_TS__TS_velocity.x = direction * SPEED\n_TS_else:\n_TS__TS_velocity.x = move_toward(velocity.x, 0, SPEED)\n\n_TS_move_and_slide()\n") },
	{ String("CharacterBody3D"), String("Basic Movement"), String("Classic movement for gravity games (FPS, TPS, ...)"), String("extends _BASE_\n\n\nconst SPEED = 5.0\nconst JUMP_VELOCITY = 4.5\n\n\nfunc _physics_process(delta: float) -> void:\n_TS_# Add the gravity.\n_TS_if not is_on_floor():\n_TS__TS_velocity += get_gravity() * delta\n\n_TS_# Handle jump.\n_TS_if Input.is_action_just_pressed(\"ui_accept\") and is_on_floor():\n_TS__TS_velocity.y = JUMP_VELOCITY\n\n_TS_# Get the input direction and handle the movement/deceleration.\n_TS_# As good practice, you should replace UI actions with custom gameplay actions.\n_TS_var input_dir := Input.get_vector(\"ui_left\", \"ui_right\", \"ui_up\", \"ui_down\")\n_TS_var direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()\n_TS_if direction:\n_TS__TS_velocity.x = direction.x * SPEED\n_TS__TS_velocity.z = direction.z * SPEED\n_TS_else:\n_TS__TS_velocity.x = move_toward(velocity.x, 0, SPEED)\n_TS__TS_velocity.z = move_toward(velocity.z, 0, SPEED)\n\n_TS_move_and_slide()\n") },
	{ String("EditorPlugin"), String("Plugin"), String("Basic plugin template"), String("@tool\nextends _BASE_\n\n\nfunc _enable_plugin() -> void:\n_TS_# Add autoloads here.\n_TS_pass\n\n\nfunc _disable_plugin() -> void:\n_TS_# Remove autoloads here.\n_TS_pass\n\n\nfunc _enter_tree() -> void:\n_TS_# Initialization of the plugin goes here.\n_TS_pass\n\n\nfunc _exit_tree() -> void:\n_TS_# Clean-up of the plugin goes here.\n_TS_pass\n") },
	{ String("EditorScenePostImport"), String("Basic Import Script"), String("Basic import script template"), String("@tool\nextends _BASE_\n\n\n# Called by the editor when a scene has this script set as the import script in the import tab.\nfunc _post_import(scene: Node) -> Object:\n_TS_# Modify the contents of the scene upon import.\n_TS_return scene # Return the modified root node when you're done.\n") },
	{ String("EditorScenePostImport"), String("No Comments"), String("Basic import script template (no comments)"), String("@tool\nextends _BASE_\n\n\nfunc _post_import(scene: Node) -> Object:\n_TS_return scene\n") },
	{ String("EditorScript"), String("Basic Editor Script"), String("Basic editor script template"), String("@tool\nextends _BASE_\n\n\n# Called when the script is executed (using File -> Run in Script Editor).\nfunc _run() -> void:\n_TS_pass\n") },
	{ String("Node"), String("Default"), String("Base template for Node with default Godot cycle methods"), String("extends _BASE_\n\n\n# Called when the node enters the scene tree for the first time.\nfunc _ready() -> void:\n_TS_pass # Replace with function body.\n\n\n# Called every frame. 'delta' is the elapsed time since the previous frame.\nfunc _process(delta: float) -> void:\n_TS_pass\n") },
	{ String("Object"), String("Empty"), String("Empty template suitable for all Objects"), String("extends _BASE_\n") },
	{ String("RichTextEffect"), String("Default"), String("Base template for rich text effects"), String("@tool\n# Having a class name is handy for picking the effect in the Inspector.\nclass_name RichText_CLASS_\nextends _BASE_\n\n\n# To use this effect:\n# - Enable BBCode on a RichTextLabel.\n# - Register this effect on the label.\n# - Use [_CLASS_SNAKE_CASE_ param=2.0]hello[/_CLASS_SNAKE_CASE_] in text.\nvar bbcode := \"_CLASS_SNAKE_CASE_\"\n\n\nfunc _process_custom_fx(char_fx: CharFXTransform) -> bool:\n_TS_var param: float = char_fx.env.get(\"param\", 1.0)\n_TS_return true\n") },
	{ String("VisualShaderNodeCustom"), String("Basic"), String("Visual shader's node plugin template"), String("@tool\n# Having a class name is required for a custom node.\nclass_name VisualShaderNode_CLASS_\nextends _BASE_\n\n\nfunc _get_name() -> String:\n_TS_return \"_CLASS_\"\n\n\nfunc _get_category() -> String:\n_TS_return \"\"\n\n\nfunc _get_description() -> String:\n_TS_return \"\"\n\n\nfunc _get_return_icon_type() -> PortType:\n_TS_return PORT_TYPE_SCALAR\n\n\nfunc _get_input_port_count() -> int:\n_TS_return 0\n\n\nfunc _get_input_port_name(port: int) -> String:\n_TS_return \"\"\n\n\nfunc _get_input_port_type(port: int) -> PortType:\n_TS_return PORT_TYPE_SCALAR\n\n\nfunc _get_output_port_count() -> int:\n_TS_return 1\n\n\nfunc _get_output_port_name(port: int) -> String:\n_TS_return \"result\"\n\n\nfunc _get_output_port_type(port: int) -> PortType:\n_TS_return PORT_TYPE_SCALAR\n\n\nfunc _get_code(input_vars: Array[String], output_vars: Array[String],\n_TS__TS_mode: Shader.Mode, type: VisualShader.Type) -> String:\n_TS_return output_vars[0] + \" = 0.0;\"\n") },
};
