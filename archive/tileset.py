# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]
#Initializing Map object
site_map = folium.Map(
    location=nasa_coordinate,
    zoom_start=7,
    tiles=None
)

# Base Dark Tile Layer
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Dark Gray",
    name="Dark Canvas (Presentation)",
    max_zoom=16
).add_to(site_map)

# High-Detail Infrastructure / Satellite Layer
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Satellite",
    name="Satellite (To Spot Rails)",
    max_zoom=19
).add_to(site_map)

# Standard OSM (Explicit railway lines)
folium.TileLayer(
    tiles="OpenStreetMap",
    name="OpenStreetMap (Clear Rail Lines)"
).add_to(site_map)

#Layer Switcher
folium.LayerControl(collapsed=False).add_to(site_map)



# OLD
# # Start location is NASA Johnson Space Center
# nasa_coordinate = [29.559684888503615, -95.0830971930759]
# # site_map = folium.Map(location=nasa_coordinate, zoom_start=10)
# # Initializing map
# site_map = folium.Map(location=nasa_coordinate, zoom_start=5, tiles=None)

# # 1. Esri Base Dark Gray Layer
# folium.TileLayer(
#     tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}",
#     attr="Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
#     name="Esri Dark Gray",
#     max_zoom=16,
# ).add_to(site_map)

# # 2. Reference Labels Layer
# folium.TileLayer(
#     tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}",
#     attr="Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
#     name="Esri Dark Gray Labels",
#     overlay=True,
#     max_zoom=16,
# ).add_to(site_map)

# # 3. Adding launch site indicators and styled labels
# # Color Scheme: Aerospace Cyberpunk / Data Vis (Vivid Amber/Orange or Cyan)
# theme_color = "#00e5ff"       # High-contrast Cyan (Alternative: '#ff9100' for aerospace amber)
# bg_badge = "rgba(18, 18, 18, 0.75)"
#
#
#Basic theme for initial markings
theme_color = "#00e5ff"       # High-contrast Cyan (Alternative: '#ff9100' for aerospace amber)
bg_badge = "rgba(18, 18, 18, 0.75)"


#Basic theme for initial markings
theme_color = "#00e5ff"       # High-contrast Cyan (Alternative: '#ff9100' for aerospace amber)
bg_badge = "rgba(18, 18, 18, 0.75)"

# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
folium.Circle(
    location=nasa_coordinate,
    radius=1000,
    color=theme_color,
    fill=True,
    popup='Nasa Johnson Space Center'
).add_to(site_map)

label_html = f"""
    <div style="
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: {theme_color};
        background: {bg_badge};
        border: 1px solid {theme_color}44;
        border-radius: 4px;
        padding: 2px 7px;
        white-space: nowrap;
        box-shadow: 0 2px 6px rgba(0,0,0,0.6);
        pointer-events: none;
    ">
        NASA JSC
    </div>
    """

folium.Marker(
    location=nasa_coordinate,
    icon=DivIcon(
            icon_size=(150, 24),    # Explicit bounding box prevents truncation
            icon_anchor=(-10, 12),  # Offsets label 10px to the right and vertically centered
            html=label_html,
        )
).add_to(site_map)

if not os.path.exists('../maps/basewcircles.html'):
    site_map.save('../maps/basewcircles.html')

site_map


# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]
#Initializing Map object
site_map = folium.Map(
    location=nasa_coordinate,
    zoom_start=7,
    tiles=None
)

# Base Dark Tile Layer
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Dark Gray",
    name="Dark Canvas (Presentation)",
    max_zoom=16
).add_to(site_map)

# High-Detail Infrastructure / Satellite Layer
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Satellite",
    name="Satellite (To Spot Rails)",
    max_zoom=19
).add_to(site_map)

# Standard OSM (Explicit railway lines)
folium.TileLayer(
    tiles="OpenStreetMap",
    name="OpenStreetMap (Clear Rail Lines)"
).add_to(site_map)

#Layer Switcher
folium.LayerControl(collapsed=False).add_to(site_map)







color_map = {
    "green": "#00e676",  # High-luminance neon green
    "red": "#ff3366",    # High-luminance electric red
}
default_color = "#00e5ff"

for row in spacex_df.itertuples():
    raw_color = row.marker_color
    accent_color = color_map.get(raw_color, default_color)

    folium.Marker(
        location=[row.Lat, row.Long],
        popup=folium.Popup(row[1] ,parse_html=True),
        icon=folium.Icon(
            color="white",           # Dark pin shell blends with the dark base map
            icon_color=row.marker_color, # High-contrast neon glyph
            icon="info-sign",           # Relevant FontAwesome/Glyphicon icon
            # prefix="fa"
        )
    ).add_to(marker_cluster)
site_map.add_child(marker_cluster)

site_map
