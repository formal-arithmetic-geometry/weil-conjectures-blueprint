+++
id = "lemma-unramified-at-infinity-no-linear-characters--1"
kind = "lemma"
title = "The zero and nonzero linear characters"
order = 1270001
aliases = ["bp-r392-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isGeometricallyConstant_of_hasLinearArtinSchreierConstituent_zero", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.not_hasLinearArtinSchreierConstituent_of_isUnramifiedAtInfinity'"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-weil-structure--1", "definition-weil-structure--3", "definition-compactification-refinement--1"]
+++
Let $k_0$ be a finite field of characteristic $p$, let $\ell\ne p$ be
prime, and let $M$ be a lisse Weil $\overline{\mathbf Q}_\ell$-sheaf on a
dense open $U_0\subset\mathbf A^1_{k_0}$. Put
$U=U_0\otimes_{k_0}\bar k_0$, and let
$\psi:k_0\to\overline{\mathbf Q}_\ell^\times$ be an additive character.

1. If $M$ is irreducible and $\mathcal L_{\psi(0x)}|_U$ is a geometric
   constituent of $M$, then $M$ is geometrically constant. This assertion
   does not require $\psi$ to be nontrivial or $M$ to be unramified at infinity.
2. If $\psi$ is nontrivial and $M$ is unramified at infinity, then no
   geometric constituent of $M$ is $\mathcal L_{\psi(ax)}|_U$ for
   $a\in\bar k_0^\times$. This assertion does not require $M$ to be irreducible.

Here a geometric constituent is a quotient of a lisse subsheaf of $M|_U$.
Unramifiedness at infinity means that $M$ extends to a lisse Weil sheaf on
$U_0\cup\{\infty\}\subset\mathbf P^1_{k_0}$, and geometric constancy means
that $M|_U$ is a finite direct sum of copies of $\overline{\mathbf Q}_\ell$.

In particular, if $\psi$ is nontrivial and $M$ is irreducible, unramified
at infinity and not geometrically constant, then no geometric constituent
of $M$ is of the form $\mathcal L_{\psi(ax)}|_U$ with $a\in\bar k_0$.
