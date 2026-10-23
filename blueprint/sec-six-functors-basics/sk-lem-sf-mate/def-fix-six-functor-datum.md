+++
id = "def-fix-six-functor-datum"
kind = "definition"
title = "Six-functor datum"
order = 2342
uses = ["def-compact-support-direct-image-detailed", "def-exchange-projection", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-extension-by-zero", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-compactification-coherence-detailed", "det-def-sfb-bounded-constructible", "sk-def-sfb-dc-lower-shriek", "sk-def-sfb-dc-upper-shriek", "sk-thm-existence", "sk-thm-sf-comp-composition"]
+++
Fix the global finite-field datum
$(p,a,q,k_0,k)$, a prime $\ell\neq p$, a finite extension
$E/\Ql$ with valuation ring $\mathcal O_E$ and uniformizer
$\pi_E$, and $n\in\mathbf Z_{\geq1}$; put
$A=A_{E,n}$ and $\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$. The rings
$\mathcal O_E,E,\Qlb$ are regarded as condensed rings, and
$D^b_c(-,\Lambda)$ is the condensed bounded constructible category
([det-def-sfb-bounded-constructible]); at the finite ring $A$ the
finite-torsion constructibility convention applies. Let $X,Y$ be
finite-type $k$-schemes,
let $f:X\to Y$ be a
separated morphism of
finite type, and let $j:U\hookrightarrow X$ be an
open immersion. On the
small pro-etale sites use the
bounded constructible categories $D^b_c(-,\Lambda)$ and the
finite-Tor subcategories
$D^b_{ctf}(-,\Lambda)$. The *six-functor operation datum* of the blueprint
consists of:

1. the derived pullback $Lf^*$, the derived tensor
$-\otimes^L_{\Lambda}-$, and the derived internal Hom
$R\mathcal Hom_{\Lambda}(-, -)$, and the derived direct image
$Rf_*$;
1. the extension-by-zero functor $j_!$, and the
compact-support direct image $Rf_!$: the compactification
independent compact-support direct image at the finite level and,
at $\mathcal O_E,E,\Qlb$, the condensed functor $Rf_!=Rp_*\circ i_!$ of
[sk-def-sfb-dc-lower-shriek], with the compactification-comparison
isomorphisms and
the composition law
$R(g\circ f)_!\xrightarrow{\sim}Rg_!Rf_!$ ([sk-thm-sf-comp-composition] (1)); when $f$ is
proper, the
identification $Rf_!\xrightarrow{\sim}Rf_*$ is the one of
[def-compact-support-direct-image-detailed] for the compactification
$j=\operatorname{id}$, $p=f$;
1. the exchange transformations $\operatorname{Ex}_*$ and
$\operatorname{Ex}_!$ and the projection transformation
$\operatorname{PF}$;
1. the exceptional inverse image
$$
Rf^!:D^b_c(Y,\Lambda)\longrightarrow D^b_c(X,\Lambda),
$$
the right adjoint of $Rf_!$ on the bounded constructible categories, as in
the exceptional inverse
image notation [def-weil-exceptional-inverse-image]: at the finite level the
constructible exceptional adjoint, transported from the etale one, and at
$\mathcal O_E,E,\Qlb$ the condensed right adjoint of [sk-thm-existence]
(3)–(4), equivalently $i^*\circ Rp^!$ of [sk-def-sfb-dc-upper-shriek];
1. the dualizing objects $\omega_{X,\Lambda}=Ra_X^!\Lambda$ and
the Verdier dual $D_X(-)=R\mathcal Hom_{\Lambda}(-,\omega_{X,\Lambda})$,
formed from the exceptional adjoint and the derived internal Hom already
listed above, for every separated finite-type $X$.

The existence and adjunction of the constructible exceptional adjoint
$Rf^!$, its interval boundedness, its finite-Tor preservation, and the
refinement compatibility of its units and counits are theorems for every
separated finite-type morphism of finite-type $k$-schemes; the ambient notion
of [def-weil-exceptional-adjoint-admissibility] is not assumed, its clause (1)
being false in general.
