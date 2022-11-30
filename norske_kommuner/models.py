# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2022-12-04T17:32:23+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Model(BaseModel):
    __root__: Any


class FylkerEnkel(BaseModel):
    fylkesnavn: Optional[str] = Field(None, description='Navn (norsk) på et fylke')
    fylkesnummer: Optional[str] = Field(
        None,
        description='Nummerering av fylke. Tekstverdi som må bestå av 2 tall. 03 er for eksempel gyldig, mens 3 er ikke gyldig.',
    )


class KomEnkel(BaseModel):
    kommunenavn: Optional[str] = None
    kommunenummer: Optional[str] = Field(
        None,
        description='Nummerering av kommuner. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig.',
    )


class KomEnkelNorskNavn(BaseModel):
    kommunenavn: Optional[str] = None
    kommunenavnNorsk: Optional[str] = None
    kommunenummer: Optional[str] = Field(
        None,
        description='Nummerering av kommuner. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig.',
    )


class KommuneFylkeEnkel(BaseModel):
    fylkesnavn: Optional[str] = Field(None, description='Navn (norsk) på et fylke')
    fylkesnummer: Optional[str] = Field(
        None,
        description='Nummerering av fylke. Tekstverdi som må bestå av 2 tall. 03 er for eksempel gyldig, mens 3 er ikke gyldig.',
    )
    kommunenavn: Optional[str] = None
    kommunenummer: Optional[str] = Field(
        None,
        description='Nummerering av kommuner. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig.',
    )


class NavnFull(BaseModel):
    navn: Optional[str] = None
    prioritet: Optional[int] = None
    sprak: Optional[str] = None


class GeoJsonEpsg(BaseModel):
    name: Optional[str] = None


class GeoJsonCrs(BaseModel):
    properties: Optional[GeoJsonEpsg] = None
    type: Optional[str] = None


class GeoJsonPoly(BaseModel):
    coordinates: Optional[List[List[List[float]]]] = None
    crs: Optional[GeoJsonCrs] = None
    type: Optional[str] = None


class GeoJsonRaw(BaseModel):
    coordinates: Optional[List] = None
    crs: Optional[GeoJsonCrs] = None
    type: Optional[str] = None


class FylkerEnkelOmrade(BaseModel):
    fylkesnavn: Optional[str] = Field(None, description='Navn (norsk) på et fylke')
    fylkesnummer: Optional[str] = Field(
        None,
        description='Nummerering av fylke. Tekstverdi som må bestå av 2 tall. 03 er for eksempel gyldig, mens 3 er ikke gyldig.',
    )
    omrade: Optional[GeoJsonRaw] = None


class FylkerKommunerEnkel(BaseModel):
    avgrensningsboks: Optional[GeoJsonPoly] = None
    fylkesnavn: Optional[str] = Field(None, description='Navn (norsk) på et fylke')
    fylkesnummer: Optional[str] = Field(
        None,
        description='Nummerering av fylke. Tekstverdi som må bestå av 2 tall. 03 er for eksempel gyldig, mens 3 er ikke gyldig.',
    )
    kommuner: Optional[List[KomEnkel]] = None


class KomEnkelOmrade(BaseModel):
    kommunenavn: Optional[str] = None
    kommunenummer: Optional[str] = Field(
        None,
        description='Nummerering av kommuner. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig.',
    )
    omrade: Optional[GeoJsonRaw] = None


class GeoJson(BaseModel):
    coordinates: Optional[List[float]] = None
    crs: Optional[GeoJsonCrs] = None
    type: Optional[str] = None


class GeoJsonFeature(BaseModel):
    geometry: Optional[GeoJsonRaw] = None
    properties: Optional[KomEnkel] = None
    type: Optional[str] = None


class GeoJsonFeatureCollection(BaseModel):
    features: Optional[List[GeoJsonFeature]] = None
    type: Optional[str] = None


class KomFull(BaseModel):
    avgrensningsboks: Optional[GeoJsonPoly] = None
    fylkesnavn: Optional[str] = Field(None, description='Navn (norsk) på et fylke')
    fylkesnummer: Optional[str] = Field(
        None,
        description='Nummerering av fylke. Tekstverdi som må bestå av 2 tall. 03 er for eksempel gyldig, mens 3 er ikke gyldig.',
    )
    gyldigeNavn: Optional[List[NavnFull]] = None
    kommunenavn: Optional[str] = None
    kommunenavnNorsk: Optional[str] = None
    kommunenummer: Optional[str] = Field(
        None,
        description='Nummerering av kommuner. Tekstverdi som må bestå av 4 tall. 0301 er for eksempel gyldig, mens 301 er ikke gyldig.',
    )
    punktIOmrade: Optional[GeoJson] = None
    samiskForvaltningsomrade: Optional[bool] = None


class NavnSokKommune(BaseModel):
    antallTreff: Optional[int] = None
    kommuner: Optional[List[KomFull]] = None


class FylkerKommunerFull(BaseModel):
    avgrensningsboks: Optional[GeoJsonPoly] = None
    fylkesnavn: Optional[str] = Field(None, description='Navn (norsk) på et fylke')
    fylkesnummer: Optional[str] = Field(
        None,
        description='Nummerering av fylke. Tekstverdi som må bestå av 2 tall. 03 er for eksempel gyldig, mens 3 er ikke gyldig.',
    )
    kommuner: List[KomFull]


class AlleFylkerKommunerFull(BaseModel):
    __root__: list[FylkerKommunerFull]
