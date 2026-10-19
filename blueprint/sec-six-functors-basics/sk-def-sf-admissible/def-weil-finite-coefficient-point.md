+++
id = "def-weil-finite-coefficient-point"
kind = "definition"
title = "Finite coefficient categories over a point"
lean = ["AlgebraicGeometry.ProEtale.geometricStalk"]
order = 1868
uses = ["def-weil-finite-field-fiber", "def-weil-finite-torsion-constructibility", "sk-def-sfb-condensed-ring", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-constructible", "sk-def-sfb-bounded-constructible", "sk-thm-sfb-qlbar-two-colimit"]
+++
Fix the global finite-field datum [def-weil-finite-field-fiber] $p,a,q,k_0,k$,
and fix a prime $\ell\neq p$. Write $\Ql=\mathbf Q_\ell$, choose an algebraic
closure $\Qlb$ of $\Ql$, and fix a finite extension $E/\Ql$ with valuation
ring $\mathcal O_E$, a uniformizer $\pi_E$, and $n\geq1$. Put
$A_{E,n}=\mathcal O_E/\pi_E^n$. Let $\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$,
regarded as a condensed ring ([sk-def-sfb-condensed-ring],
[sk-def-sfb-qlbar-condensed]; $A_{E,n}$ is discrete), and write
$\Lambda(*)$ for its ring of sections over the point, which is the ordinary
ring $A_{E,n}$, $\mathcal O_E$, $E$ or $\Qlb$.

Let $D^b_{\mathrm{fin}}(A_{E,n})$ be the full subcategory of $D(A_{E,n})$ of
bounded complexes with finite cohomology modules, $D^b_{\mathrm{fg}}(\mathcal
O_E)$ the full subcategory of $D(\mathcal O_E)$ of bounded complexes with
finitely generated cohomology modules, and $D^b_{\mathrm{fd}}(E)$ and
$D^b_{\mathrm{fd}}(\Qlb)$ the full subcategories of $D(E)$ and $D(\Qlb)$ of
bounded complexes with finite-dimensional cohomology. These are ordinary
derived categories of modules over the rings $\Lambda(*)$; no colimit over
finite extensions enters the definition of $D^b_{\mathrm{fd}}(\Qlb)$.

Let $s=\operatorname{Spec}k$. Since $k$ is algebraically closed, the qcqs objects
of $s_{\mathrm{proét}}$ are the spectra of the algebras of locally constant
functions on profinite sets, and a family of maps to such an object is a cover
exactly when finitely many of its members are jointly surjective (Bhatt–Scholze,
*The pro-étale topology for schemes*, Example 4.1.10). So every cover of the
final object $s$ has a section, and $\Lambda_s=p_s^*\Lambda$ ([sk-def-sfb-pulled-back-coefficients]) is free
on the final object. Hence evaluation at the geometric point $s$, that is
$\Gamma(s,-)$, is exact on $\Lambda_s$-modules, and a constructible
$\Lambda_s$-module ([sk-def-sfb-constructible]) is globally of the form
$\Lambda_s\otimes_{\Lambda(*)}P$ with $P$ finitely presented over $\Lambda(*)$,
the finite-torsion case being that of
[def-weil-finite-torsion-constructibility]. Extension of scalars
$P\mapsto\Lambda_s\otimes_{\Lambda(*)}P$ is exact (the sections of $\Lambda_s$ are
continuous functions on profinite sets, a flat $\Lambda(*)$-module) and left
adjoint to $\Gamma(s,-)$, with unit an isomorphism. Evaluation at the geometric
point therefore defines equivalences

$$
\begin{aligned}
\operatorname{Fib}_s:D^b_c(s,A_{E,n})&\xrightarrow{\sim}
D^b_{\mathrm{fin}}(A_{E,n}),&
\operatorname{Fib}_s:D^b_c(s,\mathcal O_E)&\xrightarrow{\sim}
D^b_{\mathrm{fg}}(\mathcal O_E),\\
\operatorname{Fib}_s:D^b_c(s,E)&\xrightarrow{\sim}D^b_{\mathrm{fd}}(E),&
\operatorname{Fib}_s:D^b_c(s,\Qlb)&\xrightarrow{\sim}
D^b_{\mathrm{fd}}(\Qlb),
\end{aligned}
$$

where $D^b_c(s,\Lambda)\subset D(s_{\mathrm{proét}},\Lambda)$ is the condensed
bounded constructible category ([sk-def-sfb-bounded-constructible]), with
quasi-inverse $P\mapsto\Lambda_s\otimes_{\Lambda(*)}P$.

That a complex in $D^b_{\mathrm{fd}}(\Qlb)$, or a morphism between two such
complexes, is defined over some finite $E\subset\Qlb$ is a consequence, read
off from [sk-thm-sfb-qlbar-two-colimit] through these equivalences; it is not
part of the definition.
