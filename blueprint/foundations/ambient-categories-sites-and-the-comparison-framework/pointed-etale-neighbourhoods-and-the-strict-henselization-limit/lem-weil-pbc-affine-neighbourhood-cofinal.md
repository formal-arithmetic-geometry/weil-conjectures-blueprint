+++
id = "lem-weil-pbc-affine-neighbourhood-cofinal"
kind = "lemma"
title = "Affine neighborhoods are cofinal"
order = 1215
uses = ["def-weil-pbc-pointed-etale-neighbourhoods-detailed", "def-weil-pbc-scheme-conventions"]
+++
The full subcategory of affine [def-weil-pbc-scheme-conventions] pointed
etale neighborhoods is initial in $\mathcal N_{\bar s}$ of
[def-weil-pbc-pointed-etale-neighbourhoods-detailed], hence cofinal for the
opposite-indexed stalk colimit.

## Proof

Given $(V,\bar v)$, an affine open $V_0\subseteq V$ containing the image of
$\bar v$ gives a morphism $(V_0,\bar v)\to(V,\bar v)$; given two affine
refinements, an affine open of their fibre product around the lifted point
refines both. These two facts are exactly the nonemptiness and connectedness
of the comma categories required for initiality in the sense of
[def-weil-pbc-pointed-etale-neighbourhoods-detailed].
