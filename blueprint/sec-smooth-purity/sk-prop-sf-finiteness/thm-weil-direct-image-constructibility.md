+++
id = "thm-weil-direct-image-constructibility"
kind = "theorem"
title = "Constructibility of the direct image of a finite-type morphism"
order = 1674
uses = ["def-weil-finite-torsion-constructibility", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-direct-image", "def-weil-scheme-morphism-properties", "obl-fin-comparison", "prop-weil-pbc-comparison-direct-image", "sbc-thm-finiteness-finite-type", "thm-dg-finite-type-constructibility", "thm-sc-finite-type-torsion-cd"]
+++
Fix a prime $\ell$, let $K_0$ be a field in which $\ell$ is
invertible, and let $X,Y$ be
finite-type
$K_0$-schemes. Choose a finite extension $E/\Ql$, an integer
$n\in\mathbf Z_{\geq1}$, and put $A=A_{E,n}$, the finite coefficient
ring of
the finite-torsion
coefficient construction. Let $f:X\to Y$ be a
separated morphism of
finite type of $K_0$-schemes, and let $F$ be a constructible
$A$-module sheaf on the small etale site $X_{\Et}$. Then, for every
$q\in\mathbf Z_{\geq0}$, the higher direct image $R^qf_*F$ of
[def-weil-pbc-direct-image] is constructible on $Y_{\Et}$, and if
every geometric fibre of
$f$ has dimension at most $d\in\mathbf Z_{\geq0}$, then

$$
R^qf_*F=0\qquad(q>2d).
$$

$A_{E,n}$ is finite, annihilated by $\ell^n$, so that with
$k=K_0$ the two clauses are the finite-level finite-type instances of
the direct-image finiteness conditions of
[def-weil-pbc-constructible-direct-image-finiteness]; by
[prop-weil-pbc-comparison-direct-image] the same assertions hold
on the small pro-etale sites for the constructibility convention
recorded there.
(*Source: the finite-type constructibility statement is
decomposed in the constructibility chapter as [sbc-thm-finiteness-finite-type],
whose chain is closed by the theorem [obl-fin-comparison] –
SGA IV, Exp. XIV, Th. 1.1, whose Stacks form is Theorem 63.14.5, [Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0) – proved there according to the route of
the lecture notes of Max Mornev (Higher Direct Image of Constructible
Sheaves, 18.4.2019), the fin4-* chain of the constructibility chapter; the general
finite-type case, including an open immersion, is proved in the same
chapter by Deligne's finite-boundary induction as
[thm-dg-finite-type-constructibility], so that no open-immersion
finiteness is assumed in that chain; the
vanishing bound $q>2d$ is the cohomological-dimension bound of the
geometric fibres, Stacks Project, Etale Cohomology, Tag
[0F0P](https://stacks.math.columbia.edu/tag/0F0P), now proved for
arbitrary torsion sheaves in the Jacobian chapter as
[thm-sc-finite-type-torsion-cd]; the etale-to-pro-etale comparison is Stacks Project,
Pro-etale Cohomology, Tag [099R](https://stacks.math.columbia.edu/tag/099R).*)

## Proof

[sbc-thm-finiteness-finite-type] of the constructibility chapter, whose chain is
assembled from the finite-immersion, extension-by-zero,
boundary-sheaf, open-immersion, Nagata-compactification, and proper-case
steps, the last of which is the single input
[obl-fin-comparison], applied with
$k=K_0$, $S=X$, $T=Y$, $u=f$, and $\Lambda=A_{E,n}$, gives the
constructibility of $R^qf_*F$ on $Y_{\Et}$ for every $q\geq0$ and
the vanishing $R^qf_*F=0$ for $q>2d$, on the small etale sites,
under the constructibility conventions of
[def-weil-pbc-constructible-direct-image-finiteness]. The
pro-etale form is the transport of these two clauses by the comparison
of direct images of [prop-weil-pbc-comparison-direct-image], with
the same constructibility convention of
[def-weil-pbc-constructible-direct-image-finiteness].
