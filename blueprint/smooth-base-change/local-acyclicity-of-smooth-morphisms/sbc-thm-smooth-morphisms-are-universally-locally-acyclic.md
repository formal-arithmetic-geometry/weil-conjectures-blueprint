+++
id = "sbc-thm-smooth-morphisms-are-universally-locally-acyclic"
kind = "theorem"
title = "Smooth morphisms are universally locally acyclic"
order = 2815
uses = ["def-sbc-smooth-morphisms", "sbc-def-local-acyclicity", "sbc-lem-local-acyclicity-constant", "sbc-lem-stalk-form", "sbc-thm-smooth-base-change"]
+++
Let $f:X\to S$ be a
smooth morphism of schemes. Then
$f$ is *universally locally acyclic*.
(*Stacks Project, Proposition 59.93.2, [Tag `0GJQ`](https://stacks.math.columbia.edu/tag/0GJQ), in the
deduction of Section 59.93, [Tag `0GJM`](https://stacks.math.columbia.edu/tag/0GJM), where local acyclicity
is deduced from the smooth base change theorem.*)

## Proof

The base change of a smooth morphism is smooth, so the assertion for
arbitrary $g$ reduces to the case of smooth morphisms: the claim is
that smooth morphisms are locally acyclic. Let $\bar x$ be a geometric
point of $X$ with image $\bar s=f(\bar x)$, let $\bar t$ be a geometric
point of $\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}$, and
let $M=\mathbf Z/n\mathbf Z$ with $n$ prime to the characteristic of
the residue field of $\bar x$. Base changing $f$ by
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}\to S$ we may
assume $S=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}$.
Apply [sbc-lem-stalk-form], the stalk form of the base-change map,
to the square

$$
\begin{array}{ccc}
X & \longleftarrow & X_{\bar t}\\
f\big\downarrow & & \big\downarrow\\
S & \longleftarrow & \bar t
\end{array}
$$

and the sheaf $\underline M$: the map
$f^{-1}R^qg_*\underline M\to R^qh_*e^{-1}\underline M$ is an
isomorphism by the smooth base change theorem
[sbc-thm-smooth-base-change] (torsion of order $n$ prime to the
characteristics), so by [sbc-lem-stalk-form]

$$
H^q\bigl(F_{\bar x,\bar t},\underline M\bigr)=
H^q(\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}
\times_S\bar t,\underline M)
=H^q(\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}
\times_S\bar t,\underline M)=H^q(\bar t,\underline M),
$$

which is $M$ in degree $0$ and $0$ above because $\bar t$ is the
spectrum of a separably closed field; by
[sbc-lem-local-acyclicity-constant] $f$ is locally acyclic, and
base changes behave the same way, so $f$ is universally locally acyclic.
