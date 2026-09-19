+++
id = "def-point-coefficient-categories"
kind = "definition"
title = "Coefficient categories over a point"
order = 86
uses = ["def-filtered-two-colimit", "def-qbar-coefficient-category", "def-qbar-finext-diagram", "def-weil-base-field", "def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], and put $s=\Spec k$.
For every $n\geq1$, let
$D^b_{\mathrm{fin}}(\mathcal O_E/\varpi_E^n)$ be the category of
bounded complexes with finite cohomology modules, let
$D^b_{\mathrm{fg}}(\mathcal O_E)$ be the category of bounded
derived-complete complexes with finitely generated cohomology, and let
$D^b_{\mathrm{fd}}(E)$ be the bounded derived category of
finite-dimensional $E$-vector spaces. For every
$E'\in\mathcal E_\ell$, the canonical equivalence
$D^b_c(s,E')\simeq D^b_{\mathrm{fd}}(E')$ identifies the constructible
transition functor for $E'\subset L$ with
$K\mapsto K\otimes^L_{E'}L$; derived-tensor associativity supplies its
unit, tower, and shift coherence. Define

$$
D^b_{\mathrm{fd}}(\Qlb)=
D^b_c(s,\Qlb).
$$

Equivalently, this is the common-stage pair category
$\operatorname{2-colim}^{\mathrm{pair}}_{E'\in\mathcal E_\ell} D^b_{\mathrm{fd}}(E')$ for the displayed transition datum.
