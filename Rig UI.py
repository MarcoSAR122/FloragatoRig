### RigUI Script generated by Bone Manager Addon ###

import bpy

from bpy.utils import register_class, unregister_class

BM_rig_id = "BM_qcnamkl1bcu4"


class BM_PT_rigui_BM_qcnamkl1bcu4(bpy.types.Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_category = 'Item'
	bl_label = "Rig UI"
	bl_idname = "BM_PT_rigui_BM_qcnamkl1bcu4"


	@classmethod
	def poll(self, context):
		try:
			return (context.active_object.data.get("BM_rig_id") == BM_rig_id)
		except (AttributeError, KeyError, TypeError):
			return False

	def draw(self, context):
		arm = context.active_object.data
		bcolls = arm.collections_all
		layout = self.layout
		layout = layout.column()
		row = layout.row(align=True)

		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Switch"], "is_solo", toggle=True, text="Switch")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Switch"
		op.arm_name = context.active_object.name

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Complement"], "is_solo", toggle=True, text="Complement")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Complement"
		op.arm_name = context.active_object.name

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Root"], "is_solo", toggle=True, text="Root")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Root"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)
		row.separator(factor=1.5)
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Spine"], "is_solo", toggle=True, text="Spine")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Spine"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Hair"], "is_solo", toggle=True, text="Hair")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Hair"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Tail"], "is_solo", toggle=True, text="Tail")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Tail"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Cloth"], "is_solo", toggle=True, text="Cloth")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Cloth"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Shoulders"], "is_solo", toggle=True, text="Shoulders")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Shoulders"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Ears"], "is_solo", toggle=True, text="Ears")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Ears"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Facial"], "is_solo", toggle=True, text="Facial")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Facial"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Eye"], "is_solo", toggle=True, text="Eye")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Eye"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Fingers"], "is_solo", toggle=True, text="Fingers")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Fingers"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)
		row.separator(factor=1.5)
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Arm IK Control"], "is_solo", toggle=True, text="Arm IK Control")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Arm IK Control"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["R Arm IK"], "is_solo", toggle=True, text="R Arm IK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "R Arm IK"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["L Arm IK"], "is_solo", toggle=True, text="L Arm IK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "L Arm IK"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Leg IK Control"], "is_solo", toggle=True, text="Leg IK Control")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Leg IK Control"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["R Leg IK"], "is_solo", toggle=True, text="R Leg IK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "R Leg IK"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["L Leg IK"], "is_solo", toggle=True, text="L Leg IK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "L Leg IK"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)
		row.separator(factor=1.5)
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Arm FK Control"], "is_solo", toggle=True, text="Arm FK Control")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Arm FK Control"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["R Arm FK"], "is_solo", toggle=True, text="R Arm FK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "R Arm FK"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["L Arm FK"], "is_solo", toggle=True, text="L Arm FK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "L Arm FK"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Leg FK Control"], "is_solo", toggle=True, text="Leg FK Control")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Leg FK Control"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["R Leg FK"], "is_solo", toggle=True, text="R Leg FK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "R Leg FK"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["L Leg FK"], "is_solo", toggle=True, text="L Leg FK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "L Leg FK"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)
		row.separator(factor=1.5)
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Yo-yo Claw"], "is_solo", toggle=True, text="Yo-yo Claw")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Yo-yo Claw"
		op.arm_name = context.active_object.name
		row = layout.row(align=True)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Yo-yo Struture"], "is_solo", toggle=True, text="Yo-yo Struture")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Yo-yo Struture"
		op.arm_name = context.active_object.name
		slot.separator(factor=2)

		slot = row.row(align=True)
		button = slot.row(align=True)
		button.prop(bcolls["Yo-yo IK"], "is_solo", toggle=True, text="Yo-yo IK")
		picker = slot.row(align=True)
		op = picker.operator("bonemanex.collection_select", text="", icon="RESTRICT_SELECT_OFF")
		op.bcoll_name = "Yo-yo IK"
		op.arm_name = context.active_object.name


class BM_PT_dynamicPanel_BM_qcnamkl1bcu4(bpy.types.Panel):
	bl_category = 'Item'
	bl_label = "Dynamic Panel"
	bl_idname = "BM_PT_dynamicPanelBM_qcnamkl1bcu4"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_options = {'DEFAULT_CLOSED'}

	@classmethod
	def poll(self, context):
		try:
			return (context.active_object.data.get("BM_rig_id") == BM_rig_id)
		except (AttributeError, KeyError, TypeError):
			return False

	def draw(self, context):
		layout = self.layout
		ob = context.active_object
		arm = ob.data
		panels = arm.prop_collection

		header, panel = layout.panel('Complement', default_closed=False)
		header.label(text='Complement')
		if panel:
			box = panel.box()
			row= box.row(align=True)
			row.label(text = 'Head Follow')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["Head_Follow"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'Head Follow Parent')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["Head_Follow_Parent"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'Floragato Skin')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["Floragato Skin"]', text = '', emboss=True, toggle=True, slider=True)

		header, panel = layout.panel('Arm Controls', default_closed=False)
		header.label(text='Arm Controls')
		if panel:
			box = panel.box()
			row= box.row(align=True)
			row.label(text = 'L Arm FK -> IK')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["L_Arm FK -> IK"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'L Arm Pivot Parent')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["L_Arm Pivot Parent"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'R Arm FK -> IK')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["R_Arm FK -> IK"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'R Arm Pivot Parent')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["R_Arm Pivot Parent"]', text = '', emboss=True, toggle=True, slider=True)

		header, panel = layout.panel('Leg Controls', default_closed=False)
		header.label(text='Leg Controls')
		if panel:
			box = panel.box()
			row= box.row(align=True)
			row.label(text = 'L Leg IK -> FK')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["L_Leg IK -> FK"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'L Leg Pivot Parent')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["L_Leg Pivot Parent"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'R Leg IK -> FK')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["R_Leg IK -> FK"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'R Leg Pivot Parent')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["R_Leg Pivet Parent"]', text = '', emboss=True, toggle=True, slider=True)

		header, panel = layout.panel('Yo-yo', default_closed=False)
		header.label(text='Yo-yo')
		if panel:
			box = panel.box()
			row= box.row(align=True)
			row.label(text = 'Yo-yo BASE')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["Yo-yo BASE"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'Yo-yo Inter')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["Yo-yo Inter"]', text = '', emboss=True, toggle=True, slider=True)

			row= box.row(align=True)
			row.label(text = 'Yo-yo Spine')
			row.prop(bpy.data.objects['Floragato'].pose.bones['head.001'], '["Yo-yo Spine"]', text = '', emboss=True, toggle=True, slider=True)



class BM_PT_customprops_BM_qcnamkl1bcu4(bpy.types.Panel):
	bl_category = 'Item'
	bl_label = "Rig Properties"
	bl_idname = "BM_PT_customprops_BM_qcnamkl1bcu4"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_options = {'DEFAULT_CLOSED'}

	@classmethod
	def poll(self, context):
		if context.active_object.data.get('BM_rig_id'):
			pose_bones = context.selected_pose_bones
			props = None
			rna_properties = {prop.identifier for prop in bpy.types.PoseBone.bl_rna.properties if prop.is_runtime}
			if context.selected_pose_bones:
				bones = context.selected_pose_bones

			elif context.selected_editable_bones:
				bones = [pose_bones[bone.name] for bone in context.selected_editable_bones]

			elif context.mode == 'OBJECT':
				bones = context.active_object.pose.bones

			else:
				return False
			if bones:
				props = [[prop for prop in bone.items() if prop not in rna_properties] for bone in bones]

			if props and bones:
				return (context.active_object.data.get("BM_rig_id") == BM_rig_id)
			else:
				return False

		else:
			return False

	def draw(self, context):
		layout = self.layout
		pose_bones = context.active_object.pose.bones
		if context.selected_pose_bones:
			bones = context.selected_pose_bones

		elif context.selected_editable_bones:
			bones = [pose_bones[bone.name] for bone in context.selected_editable_bones]

		else:
			bones = context.active_object.pose.bones

		def assign_props(row, val, key):
			row.property = key
			row.data_path = "active_pose_bone"
			try:
				row.value = str(val)
			except:
				pass

		rna_properties = {
			prop.identifier for prop in bpy.types.PoseBone.bl_rna.properties
			if prop.is_runtime
		}

		skip_keys = rna_properties

	# Iterate through selected bones add each prop property of each bone to the panel.
		if context.selected_pose_bones is not None:
			for bone in context.selected_pose_bones:
				for i, in enumerate(sorted(bone.keys())):
					if key not in skip_keys:
						if i == 0:
							box = layout.box()
						val = bone.get(key, "value")
						row = box.row()
						split = row.split(align=True, factor=0.7)
						row = split.row(align=True)
						row.label(text=key, translate=False)
						row = split.row(align=True)
						row.prop(bone, f'["{key}"]', text = "", slider=True)


def get_bones(arm, context, collection, selected):
	if collection:
		bones = arm.collections_all[collection.name].bones
		if selected:
			try:
				bones = [bone for bone in bones if bone.select is True]
			except TypeError:
				return []
	elif selected and not collection:
		try:
			bones = [bone for bone in arm.bones if bone.select is True]
		except TypeError:
			return []
	else:
		bones = arm.bones
	return bones


class BMEX_OT_selectCollection(bpy.types.Operator):
	bl_idname = "bonemanex.collection_select"
	bl_label = ""
	bl_description = "Select all Bones in Collection.\nShift to add to selection. \nAlt to remove from selection"

	bcoll_name : bpy.props.StringProperty(name="Collection name", description="Name of bone collection", default="",)
	arm_name : bpy.props.StringProperty(name="Armature name", description="Name of armature", default="",)

	@classmethod
	def poll(self, context):

		return context.mode == "POSE"

	def __init__(self):
		self.shift = False
		self.alt = False

	def invoke(self, context, event):
		self.shift = event.shift
		self.alt = event.alt

		return self.execute(context)

	def execute(self, context):
		ob = context.active_object
		arm = ob.data
		bcolls = arm.collections_all
		bcoll = arm.collections_all[self.bcoll_name]

		if self.alt:
			bones = get_bones(arm, context, bcoll, True)
			for bone in bones:
				bone.select = False
				bone.select_head = False
				bone.select_tail = False

		else:
			bones = get_bones(arm, context, bcoll, False)
			if not self.shift:
				bpy.ops.pose.select_all(action="DESELECT")

			for bone in bones:
				bone.select = True
				bone.select_head = True
				bone.select_tail = True

		return {"FINISHED"}


classes = (BM_PT_rigui_BM_qcnamkl1bcu4,BMEX_OT_selectCollection, BM_PT_customprops_BM_qcnamkl1bcu4, BM_PT_dynamicPanel_BM_qcnamkl1bcu4, BMEX_OT_selectCollection)

def register():
	for cls in classes:
		try:
			register_class(cls)

		except ValueError:
			pass
def unregister():
	for cls in classes:
		try:
			unregister_class(cls)

		except ValueError:
			pass


	del bpy.types.Scene.BM_qcnamkl1bcu4_presets

if __name__ == "__main__":
	register()