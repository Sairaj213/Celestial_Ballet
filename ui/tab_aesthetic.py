import streamlit as st

def render_tab_aesthetic():

    st.title("🎨 Aesthetic Controls")
    st.markdown("Customize the look and feel of the simulation lab.")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Color & Theme")
        st.selectbox(
            "UI Theme",
            options=["System Default", "Light", "Dark"],
            index=2, 
            help="Note: This is a conceptual control. For a permanent theme, set it in Streamlit's .streamlit/config.toml file."
        )

        if 'body_colors' not in st.session_state:
            st.session_state.body_colors = ['#0000FF', '#FF0000', '#00FF00'] 

        st.session_state.body_colors[0] = st.color_picker("Body 1 Color", value=st.session_state.body_colors[0])
        st.session_state.body_colors[1] = st.color_picker("Body 2 Color", value=st.session_state.body_colors[1])
        st.session_state.body_colors[2] = st.color_picker("Body 3 Color", value=st.session_state.body_colors[2])
        st.info("Color changes will apply on the next simulation run.")

    with col2:
        st.subheader("Plotting & Animation")
        st.slider(
            "Trajectory Trail Length (%)", 
            min_value=10, 
            max_value=100, 
            value=st.session_state.get('trail_length', 100),
            key='trail_length',
            help="Determines how much of the past trajectory is visible."
        )
        
        st.selectbox(
            "Camera Mode (3D Plot)",
            options=["Turntable (Auto-Rotate)", "Static", "Follow Body 1"],
            key='camera_mode',
            help="Conceptual control for the 3D visualization."
        )
        
        st.toggle(
            "Show Velocity Vectors",
            value=st.session_state.get('show_vectors', False),
            key='show_vectors',
            help="Display arrows indicating the current velocity of each body."
        )