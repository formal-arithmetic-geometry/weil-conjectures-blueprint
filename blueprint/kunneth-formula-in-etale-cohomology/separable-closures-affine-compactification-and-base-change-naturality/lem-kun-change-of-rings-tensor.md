+++
id = "lem-kun-change-of-rings-tensor"
kind = "lemma"
title = "Change of rings for the derived tensor"
order = 6109
lean = ["AlgebraicGeometry.Etale.derivedTensor_changeOfRings"]
uses = ["def-kun-derived-tensor", "def-kun-torsion-invertible"]
+++
Let $\Lambda'=\mathbf Z/n\mathbf Z$, let $M$ be a flat
$\Lambda'$-module, let $n=\ell m$ with $\ell$ a prime dividing $n$, and let
$N$ be a complex of $\Lambda'$-modules annihilated degreewise by $\ell$,
viewed as a complex of $\mathbf F_\ell$-vector spaces. Then
$$
 M\otimes^{\mathbf L}_{\Lambda'}N\cong(M/\ell M)\otimes^{\mathbf L}_{\mathbf F_\ell}N
$$
canonically in $D(\mathrm{Mod}(\Lambda'))$.

## Proof

Since $M$ is flat, the derived tensor product is the underived one. The
sequence
$$
 \ell M\longrightarrow M\longrightarrow M/\ell M\longrightarrow0
$$
is right exact and, tensored with $N$, the image of
$\ell M\otimes_{\Lambda'}N$ in $M\otimes_{\Lambda'}N$ is
$\ell(M\otimes_{\Lambda'}N)=M\otimes_{\Lambda'}\ell N=0$, because $\ell N=0$;
hence $M\otimes_{\Lambda'}N=(M/\ell M)\otimes_{\Lambda'}N$, and the right side
identifies canonically with $(M/\ell M)\otimes_{\mathbf F_\ell}N$ since $\ell$
annihilates $N$ and $M/\ell M$.
