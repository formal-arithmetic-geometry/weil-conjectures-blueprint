+++
id = "def-weil-exceptional-inverse-image"
kind = "definition"
title = "Exceptional inverse image notation"
order = 1261
lean = ["AlgebraicGeometry.Proetale.upperShriek", "AlgebraicGeometry.Proetale.upperShriekAdjunction"]
uses = ["def-weil-exceptional-adjoint-admissibility", "def-weil-ambient-exceptional-adjoint", "def-weil-finite-torsion-constructibility", "def-weil-finite-tor-amplitude", "def-weil-algebraically-closed-coefficients", "def-compact-support-direct-image-detailed", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with valuation ring $\mathcal
O_E$ and uniformizer $\varpi_E$, and an integer $n\in\mathbf Z_{\geq1}$, with
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$. Let $S$ be a scheme on which $\ell$ is
invertible, let $X,Y$ be finite-type
[def-weil-scheme-morphism-properties] $S$-schemes, and let $f:X\to Y$ be a
separated finite-type $S$-morphism. Assume the ambient exceptional right
adjoint datum [def-weil-ambient-exceptional-adjoint] at every finite
coefficient stage, so that the right adjoint $Rf_n^{\times}$ of $Rf_{!,n}$
exists on the ordinary derived categories. Use finite-torsion
constructibility [def-weil-finite-torsion-constructibility] and the
compact-support direct image
[def-compact-support-direct-image-detailed]. On the small pro-etale sites
[def-weil-small-proetale-site-detailed], set

$$
 Rf_n^!=Rf_n^{\times}|_{D^b_c(Y,A_{E,n})}:
 D^b_c(Y,A_{E,n})\longrightarrow D^b_c(X,A_{E,n}).
$$

For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$, use respectively derived inverse
limits, rationalization, and the common-stage construction
[def-weil-algebraically-closed-coefficients] of the compatible finite-level
functors, and define

$$
 Rf^!:D^b_c(Y,\Lambda)\longrightarrow D^b_c(X,\Lambda).
$$

For $K\in D^b_c(X,\Lambda)$ and $L\in D^b_c(Y,\Lambda)$, characterize the
resulting functor by the natural adjunction isomorphisms

$$
 \Hom_Y(Rf_!K,L)\cong\Hom_X(K,Rf^!L).
$$

The displayed typing of the restriction, and its restriction to finite-Tor
objects [def-weil-finite-tor-amplitude], use clauses (2) and (3) of
[def-weil-exceptional-adjoint-admissibility]: these are preservation clauses,
assumed only in the chapters that apply the right adjoint to objects of those
subcategories. Of the hypothesis that the datum is assumed at every finite
coefficient stage, the existence half is not an assumption on these two
categories.
