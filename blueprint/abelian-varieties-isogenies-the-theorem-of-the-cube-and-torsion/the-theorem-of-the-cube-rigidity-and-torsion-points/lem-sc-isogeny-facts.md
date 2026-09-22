+++
id = "lem-sc-isogeny-facts"
kind = "lemma"
title = "Basic facts about isogenies"
order = 4018
lean = ["AlgebraicGeometry.AbelianVariety.isIsogeny_multByN", "AlgebraicGeometry.AbelianVariety.card_torsion"]
uses = ["def-sc-mult-n", "def-sc-abelian-variety", "def-sc-isogeny", "lem-sc-mult-n-isogeny", "lem-sc-abelian-variety-projective", "lem-sc-ample-tensor", "thm-sc-theorem-of-cube", "lem-sc-mult-n-pullback", "lem-sc-isogeny-degree", "lem-sc-deg-pullback-finite", "lem-sc-mult-n-finite-flat"]
+++
Let $A$ be an abelian variety [def-sc-abelian-variety] of dimension $g$
over an algebraically closed field $k$ and $n\geq1$.

- (a) The map $[n]$ of [def-sc-mult-n] is an isogeny [def-sc-isogeny] of
  degree $n^{2g}$, finite, flat and surjective.
- (b) In particular the kernel $A[n]$ is a finite flat group scheme of
  order $n^{2g}$ over $k$, and $[n]:A\to A$ is an fppf covering.

*Source: Stacks Project, Groupoid Schemes, Section 39.9, [Tag
0BF9](https://stacks.math.columbia.edu/tag/0BF9); in particular Lemma
39.9.2, [Tag 0BFA](https://stacks.math.columbia.edu/tag/0BFA) (abelian
varieties are projective), Lemmas 39.9.6--39.9.7, [Tag
0BFE](https://stacks.math.columbia.edu/tag/0BFE) and [Tag
0BFF](https://stacks.math.columbia.edu/tag/0BFF) (the theorem of the cube,
see also More on Morphisms, Theorem 37.33.8, [Tag
0BF4](https://stacks.math.columbia.edu/tag/0BF4)), Lemma 39.9.8, [Tag
0BFG](https://stacks.math.columbia.edu/tag/0BFG) ($[d]$ is finite locally
free of degree $d^{2\dim A}$), and Proposition 39.9.11, [Tag
03RP](https://stacks.math.columbia.edu/tag/03RP); for the degree
positivity, Stacks Project, Varieties, Lemma 33.45.9, [Tag
0BEV](https://stacks.math.columbia.edu/tag/0BEV). Cf. the classical
treatments of Mumford and Milne.*

## Proof

(a) By [lem-sc-mult-n-isogeny], the map $[n]$ of [def-sc-mult-n] is a
surjective homomorphism of group schemes with finite kernel $A[n]$, and it
is finite (as in loc. cit.); it is an isogeny in the sense of
[def-sc-isogeny]. It is flat: the fibres $[n]^{-1}(y)=x+A[n]$ are
translates of the finite scheme $A[n]$, hence all have the same length, so
the constant-fibre-length flatness lemma applies and $[n]_*\mathcal O_A$ is
locally free of rank $\deg([n])$. Thus $[n]$ is finite flat and surjective.

It remains to compute the degree. We follow the classical argument of
[lem-sc-mult-n-finite-flat]. By [lem-sc-abelian-variety-projective] $A$ is
projective, so it carries an ample line bundle, and for any ample
$\mathcal L$ the module $\mathcal N:=\mathcal L\otimes[-1]^*\mathcal L$ is
ample with $[-1]^*\mathcal N\cong\mathcal N$ [lem-sc-ample-tensor]. By
[thm-sc-theorem-of-cube] and [lem-sc-mult-n-pullback],
$[n]^*\mathcal N\cong\mathcal N^{\otimes n^2}$. Let $\deg_{\mathcal M}$ be
the Hilbert degree, so that $m\mapsto\chi(A,\mathcal N^{\otimes m})$ is the
corresponding numerical polynomial. Then
$$
 \deg_{\mathcal N^{\otimes n^2}}(A)=n^{2g}\deg_{\mathcal N}(A),
$$
because replacing $\mathcal N$ by $\mathcal N^{\otimes n^2}$ replaces
$\chi(A,\mathcal N^{\otimes m})$ by $\chi(A,\mathcal N^{\otimes mn^2})$,
which multiplies the leading coefficient of the numerical polynomial by
$n^{2g}$. By [lem-sc-deg-pullback-finite], since $[n]$ is finite
surjective,
$$
 \deg_{\mathcal N^{\otimes n^2}}(A)
 =\deg_{[n]^*\mathcal N}(A)=\deg([n])\deg_{\mathcal N}(A).
$$
Here $\deg([n])$ is the degree of the finite flat morphism $[n]$, which is
the order of the kernel $A[n]$, i.e. the degree of the isogeny $[n]$, by
[lem-sc-isogeny-degree]. Comparing the two formulas gives
$\deg([n])=n^{2g}$ (using $\deg_{\mathcal N}(A)\neq0$: for an ample
$\mathcal M$ on a proper $g$-dimensional variety over $k$,
$\deg_{\mathcal M}(X)>0$, *reference: Stacks Project, Varieties, Lemma
33.45.9, [Tag 0BEV](https://stacks.math.columbia.edu/tag/0BEV)*). This
gives (a), and (b) is immediate from the definition of the kernel
[def-sc-mult-n] and the finiteness statement.

Unresolved dependencies: lem:sc-finite-constant-length-flat, def:sc-hilbert-degree, lem:sc-hilbert-polynomial
