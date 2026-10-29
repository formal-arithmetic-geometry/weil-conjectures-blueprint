+++
id = "sec-abelian-varieties"
kind = "section"
title = "Abelian Varieties"
order = 456
+++
**Content.** This section is the tex appendix "Abelian varieties and Tate
modules". All group schemes are of finite type over a field $k$. For an
abelian variety $A$ of dimension $g$ and an integer $n$ invertible in $k$,
it shows that $A[n]$ is finite étale of rank $n^{2g}$, that $T_\ell A$ is
free of rank $2g$, and that over a finite field Frobenius has no nonzero
fixed vector on $T_\ell A$. The theorem of the cube
([sk-prop-av-cube]) is proved from triviality on fibres
([sk-lem-abelian-seesaw]) and triviality near a fibre
([sk-lem-abelian-cube-open]), by gluing along a section; the descent
form of triviality over an open cover ([sk-cor-abelian-seesaw-descent]) is
recorded but not formalized. With the rigidity lemma
([sk-prop-av-rigidity]) it gives commutativity, projectivity and
$[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}$ for a symmetric ample
$\mathcal N$ ([sk-prop-av-mult-n-pullback]). This forces $[n]$ to have
finite fibres, and a comparison of degrees gives $\deg[n]=n^{2g}$
([sk-prop-av-isogeny]). The Jacobian itself is constructed later, in
§[sec-picard-framework].

**Key results.**

- Prop [sk-prop-av-isogeny] (multiplication by $n$): $[n]$ is surjective
  and finite locally free of degree $n^{2g}$, $A[n]$ has rank $n^{2g}$, and
  both are finite étale when $n$ is invertible in $k$.
- Prop [sk-prop-av-tate-rank] (the integral Tate module):
  $A[\ell^n](\bar k)\simeq(\mathbf Z/\ell^n)^{2g}$ and
  $T_\ell A\simeq\Z_\ell^{2g}$, Galois-equivariantly and invariant under a
  larger algebraically closed field. Used in §[sec-curve-estimates],
  §[sec-purity-real-sheaves], §[sec-zeta-weil].
- Prop [sk-p-tate] (no Frobenius-fixed vector): over $\mathbf F_q$,
  $F^m-1$ is an automorphism of $V_\ell A$. Used in
  §[sec-purity-real-sheaves].

Material that the tex uses without a declaration of its own sits in the
detail layer where it is first used: curves and function fields in
[sk-prop-av-isogeny], invertible sheaves in [sk-lem-abelian-seesaw]; the
Picard group, Pic⁰, the genus and the Jacobian moved to
§[sec-picard-framework], and the $p$-linear algebra (Lang–Steinberg) to
§[sec-curve-estimates].

**References.**

- Stacks Project, the theorem of the cube and abelian varieties: `0BEZ`,
  `0BDN`, `0E0L`, `0B91`, `0BCD`, `0BED` (cube); `0B7R`, `056D`, `01RH`
  (commutativity); `0BF7`, `0B45` (projectivity); `0BFF` ($[n]^*$ of
  symmetric modules); `0BFG` ($[n]$ is finite locally free of
  degree $n^{2g}$).
- Stacks Project, general inputs: `0BUG` (global functions on proper
  geometrically integral schemes), `05P3` (products of geometrically
  integral schemes), `01I1`, `02KH` (rigidity), `02OG` (proper and
  quasi-finite implies finite).
- J. Milne, *Abelian Varieties*, §I; D. Mumford, *Abelian Varieties*, §II.6
  (rigidity lemma).
