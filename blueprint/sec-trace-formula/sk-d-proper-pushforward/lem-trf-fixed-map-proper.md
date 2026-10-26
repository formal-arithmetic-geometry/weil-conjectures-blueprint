+++
id = "lem-trf-fixed-map-proper"
kind = "lemma"
title = "The induced map of fixed schemes is proper"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.fixMapFactor", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.fixMapFactor_snd", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.isPullback_fixMapFactor", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.isClosedImmersion_fixMapFactor", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.isProper_fixMap", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.isProper_prodMap"]
order = 3469
uses = ["def-trf-borel-moore-pushforward", "def-trf-coefficient-pushforward", "def-trf-fixed-scheme", "def-trf-trace-class", "def-weil-scheme-morphism-properties", "lem-kun-proper-stability", "lem-weil-pbc-closed-immersion-proper"]
+++
Let $(f,g):(C,c)\to(D,b)$ be a proper pushforward diagram of
[def-trf-coefficient-pushforward], with induced map
$h:F_c=\operatorname{Fix}(c)\to F_b=\operatorname{Fix}(b)$. Then:

1. $h$ factors as
$$
h:\ F_c\xrightarrow{\ \kappa\ }C\times_DF_b\xrightarrow{\ \pi\ }F_b,
$$
where $\pi$ is the base change of $g$ along $i_b:F_b\to D$, and
$\kappa$ is a base change of the relative diagonal
$\Delta_{X/Y}:X\to X\times_YX$, hence a closed immersion;
1. $h$ and $q=f\times f:X\times_sX\to Y\times_sY$ are proper.

Consequently, for a correspondence $u$ on $(X,K)$ supported on $c$, with
the exceptional admissibility of $h$ and of the structure morphisms of
$F_c,F_b$, the *proper pushforward of the trace class*

$$
h_*\operatorname{Tr}_c(u):A_{F_b}\longrightarrow\omega_{F_b}
$$

is defined: it is the Borel–Moore pushforward of
[def-trf-borel-moore-pushforward] of the Borel–Moore section
$\operatorname{Tr}_c(u)$ of [def-trf-trace-class].
