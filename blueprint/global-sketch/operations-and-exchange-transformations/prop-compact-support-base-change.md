+++
id = "prop-compact-support-base-change"
kind = "theorem"
title = "Compact-support base change"
order = 65
tags = ["latex:proposition"]
uses = ["def-compact-support-exchange", "def-direct-image-exchange", "def-weil-finite-coefficient-datum", "prop-compact-support-coefficient-passage", "prop-compactification-coherence", "prop-finite-proper-base-change", "prop-ramified-coefficient-change", "thm-qbar-functor-descent"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. For every Cartesian square in
Definition [def-direct-image-exchange],
every separated finite-type $f$, and every
$K\in D^b_c(X,\Lambda)$, the component

$$
\operatorname{Ex}_!(K):Lg^*Rf_!K
\xrightarrow{\sim}Rf'_!Lg'^*K
$$

is an isomorphism. If one compactification is refined by another, the two
displayed proper-base-change/open-exchange composites agree after the
coherence isomorphism of Proposition
[prop-compactification-coherence]. Horizontal and vertical pasting of
Cartesian squares gives the corresponding composite of $\operatorname{Ex}_!$
components. Finite reduction sends this component to the finite-level
component. For every finite extension $L/E$ inside $\Qlb$, with
ramification index $e$, completed scalar extension sends it to the
$L$-coefficient component, and the ramified comparison is indexed by
$n\mapsto en$.
