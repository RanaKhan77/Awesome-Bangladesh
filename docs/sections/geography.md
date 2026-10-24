# 🗺️ Geography & open maps

<img src="../../assets/sections/banner-geography.svg" width="896" alt="🗺️ Geography & open maps banner">

> Part of **[Awesome Bangladesh](../../README.md)** · All section guides: **[index](index.md)**

Administrative boundaries, geocoding libraries and map data for Bangladesh — the division → district → upazila → union hierarchy that every BD app eventually needs. The classic datasets here are among the most widely used Bangladeshi repositories on GitHub, and for good reason: everything downstream, from delivery pricing to disaster mapping, starts with this hierarchy. Boundary files are checked for actual data content, not just a README and a logo.

**13 verified entries** · Last verified: 2026-10-25 · Rules: [curation policy](../curation-policy.md)

## The full table

| Project | What it does | Licence (as stated) | Bangladesh link |
|---|---|---|---|
| [bangladesh-geocode](https://github.com/nuhil/bangladesh-geocode) | The classic division → district → upazila → union dataset with lat/long coordinates — the first import of countless Bangladeshi apps, and the dataset most others in this table derive from. | MIT | 🟡 Diaspora |
| [bangladesh-geojson](https://github.com/ifahimreza/bangladesh-geojson) | Divisions, districts, upazilas, postcodes and full boundary GeoJSON — polygons ready for Leaflet and Mapbox, pairing naturally with geocode's point data. A model example of layered licensing done right. | MIT (code) / ODbL (OSM-derived layers) / CC-BY-4.0 (boundaries) | 🟢 BD-based |
| [geo-vault](https://github.com/imran110219/geo-vault) | The deepest coverage available in one place: all 8 divisions, 64 districts, 494 upazilas and 4,540 unions with p-codes and 2022 census population figures. | Boundaries CC-BY-3.0 IGO (HDX COD-AB / geoBoundaries) | see list |
| [laravel-bangladesh-geocode](https://github.com/devfaysal/laravel-bangladesh-geocode) | Divisions, districts, thanas and unions as a Laravel package — seed the hierarchy straight into your database instead of importing CSVs (also maintained by [sandofvega](https://github.com/sandofvega/laravel-bangladesh-geocode)). | MIT | 🟢 BD-based |
| [bd-geo-info](https://www.npmjs.com/package/bd-geo-info) | Zero-dependency TypeScript/JavaScript library for BD geography with React components — hierarchy data plus ready-made UI pieces. | MIT | 🟢 BD-based |
| [@bangladeshi/bangladesh-address](https://www.npmjs.com/package/@bangladeshi/bangladesh-address) | Divisions, districts and upazilas as structured data under the @bangladeshi npm scope — a building block for address forms that do not force users to type what a dropdown knows. | MIT | 🟡 Diaspora |
| [bangladesh-location-data](https://www.npmjs.com/package/bangladesh-location-data) | Location datasets for JavaScript apps, published on npm for direct import. | MIT | 🟢 BD-based |
| [bd-divisons-to-unions](https://github.com/Azim-Ahmed/bd-divisons-to-unions) | Division-to-union lookup data — the full ladder in one dataset for search and autocomplete use cases. | ISC | 🟢 BD-based |
| [bd-geographical-data-api](https://github.com/md-redwan-hossain/bd-geographical-data-api) | REST API for Bangladesh geographical data — serve the hierarchy over HTTP instead of bundling it into every client. | MIT | see list |
| [bd_gis](https://github.com/deluair/bd_gis) | 40-year geospatial analysis of the Sylhet haor region — a research-grade study of how the wetlands changed, useful well beyond GIS circles. | MIT | 🟡 Diaspora |
| [manchitro](https://www.npmjs.com/package/manchitro) | Typed SVG maps of all 64 Bangladesh districts (মানচিত্র = map) — drop a district map into a React dashboard without a tile server or a GIS stack. | MIT | 🟢 BD-based |
| [Geofabrik Bangladesh extract](https://download.geofabrik.de/asia/bangladesh.html) | Regularly updated OpenStreetMap extract for Bangladesh in shapefile, GeoJSON and other formats — the standard starting point for local OSM work without planet-file machinery. | ODbL (OpenStreetMap data) | 🔵 BD org / for-BD |
| [OpenStreetMap Bangladesh](https://wiki.openstreetmap.org/wiki/Bangladesh) | Community hub for Bangladesh mapping efforts and import coordination — where to find the mappers and the conventions before you build on OSM data. | CC-BY-SA (wiki) | 🔵 BD org / for-BD |

## Editor's picks

### [bangladesh-geocode](https://github.com/nuhil/bangladesh-geocode)

The canonical administrative-boundary dataset with lat/long included. When a delivery app, a disaster map or a government dashboard needs division-district-upazila-union data, this is where the import usually starts — and where the rest of this table's datasets trace their ancestry.

### [geo-vault](https://github.com/imran110219/geo-vault)

All 4,540 unions with p-codes and 2022 census population in one repository — union-level granularity with population data attached is rare even in official sources, and here it ships with cleanly licensed boundary layers.

## How this section is verified

- Every link is fetched live at verification time — dead links are removed, not kept for history.
- Bangladesh connections are evidenced (profile location, org page, or the product's own docs) — see the [scope rules](../scope-and-eligibility.md).
- Dormant items (3+ years without activity) move to the [legacy file](../../legacy.md) with their last-activity date.
- Licence information is quoted as the publisher states it; gaps are flagged with ⚠️ rather than guessed.
