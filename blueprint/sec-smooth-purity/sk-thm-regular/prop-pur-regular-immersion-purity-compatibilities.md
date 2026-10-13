+++
id = "prop-pur-regular-immersion-purity-compatibilities"
kind = "theorem"
title = "Compatibilities of purity for regular immersions"
order = 2379
tags = ["latex:proposition"]
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-frame-class", "def-pur-regular-immersion", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-frame-independence", "lem-pur-kunneth-supported", "thm-pur-diagonal-dualizing-object", "thm-pur-regular-immersion-purity"]
+++
In the situation of [thm-pur-regular-immersion-purity], the purity
isomorphism is compatible with

1. *base change* along an étale morphism $X'\to X$, and more generally
along a smooth morphism $X'\to X$ of smooth $k$-schemes: then
$Z'=Z\times_XX'$ is smooth over $Z$, hence regular, and
$Z'\hookrightarrow X'$ is a regular closed immersion of the same pure
codimension $c$ (flat base change preserves regular sequences), so the
base-changed pair is again in the situation of
[thm-pur-regular-immersion-purity]. Base change along an arbitrary
morphism of pairs would leave that situation and is not claimed;
1. *transverse composition* of regular immersions: for
$i:Z\hookrightarrow Y$ and $j:Y\hookrightarrow X$ transverse regular
immersions of codimensions $b$ and $d$, the purity isomorphisms for
$i$, $j$ and $ji$ compose with the twist additivity;
1. *cup products* (the purity class of a product of pairs is
the exterior product of the classes);
1. *finite reduction* from $A_{E,n}$ to $A_{E,n-1}$.
