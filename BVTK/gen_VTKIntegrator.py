from .core import *
TYPENAMES = []


# --------------------------------------------------------------


class BVTK_NT_RungeKutta2(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RungeKutta2'
    bl_label = 'vtkRungeKutta2'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['FunctionSet'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_RungeKutta2)
TYPENAMES.append('BVTK_NT_RungeKutta2' )


# --------------------------------------------------------------


class BVTK_NT_RungeKutta45(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RungeKutta45'
    bl_label = 'vtkRungeKutta45'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['FunctionSet'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_RungeKutta45)
TYPENAMES.append('BVTK_NT_RungeKutta45' )


# --------------------------------------------------------------


class BVTK_NT_RungeKutta4(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RungeKutta4'
    bl_label = 'vtkRungeKutta4'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['FunctionSet'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_RungeKutta4)
TYPENAMES.append('BVTK_NT_RungeKutta4' )


# --------------------------------------------------------------


menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append(BVTK_NodeCategory('VTKIntegrator', 'Integrator', items=menu_items))