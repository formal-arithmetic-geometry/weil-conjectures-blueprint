+++
id = "pointed-etale-neighbourhoods-and-the-strict-henselization-limit"
kind = "section"
title = "Pointed etale neighbourhoods and the strict henselization limit"
order = 1278
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
The strict henselization presented as a limit rather than as a black box:
pointed etale neighbourhoods [def-weil-pbc-pointed-etale-neighbourhoods-detailed],
among which the affine ones are cofinal
[lem-weil-pbc-affine-neighbourhood-cofinal], so that $\mathcal
O^{\mathrm{sh}}_{S,\bar s}$ is their filtered colimit and $S_{(\bar s)}$
their inverse limit [def-weil-pbc-strict-henselization-limit-detailed]. Fibre
products commute with that limit [lem-weil-pbc-fibre-product-limit], which is
what lets stalk computations be made after base change. Extension by zero
along an etale map [def-weil-pbc-etale-sum-extension] supplies the exact left
adjoint that makes etale restriction preserve injectives
[lem-weil-pbc-etale-restriction-injectives].
