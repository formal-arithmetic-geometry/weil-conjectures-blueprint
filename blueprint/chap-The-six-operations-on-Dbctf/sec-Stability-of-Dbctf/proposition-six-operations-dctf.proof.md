+++
kind = "proof"
of = "proposition-six-operations-dctf"
order = 619
uses = ["lemma-flat-models-generators", "proposition-proper-direct-image-constructible-complexes", "theorem-exceptional-inverse-image", "lemma-inverse-image-tensor-product", "proposition-open-direct-image-preserves-finite", "proposition-direct-image-along-open-immersion"]
+++
We treat the operations in the order in which they depend on each other:
first the local operations $f^*$ and $\otimes^{\mathbf L}$, then the two
direct images, and finally internal Hom, which we express through the
others.

Pullback and tensor product preserve the property of being, on the strata
of a finite stratification, locally $\Lambda_S\otimes P$ with $P$ a perfect
complex. For pullback this is clear, since the strata pull back to a
stratification. For tensor products we take a common refinement of the two
stratifications, and on each of its strata we use that
$P\otimes^{\mathbf L}Q$ is perfect when $P$ and $Q$ are. Extension by zero
preserves finite Tor amplitude, since it is exact and satisfies the
projection formula $a_!K\otimes^{\mathbf L}N\simeq a_!(K\otimes^{\mathbf L}a^*N)$.
For finite $A$ these statements can be checked on the bounded flat
constructible models of Lemma [lemma-flat-models-generators]. For
$\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ they follow from Lemma [lemma-inverse-image-tensor-product] and
from Definition [definition-constructible-sheaves] of constructible sheaves: on each stratum, such a sheaf is
locally $\Lambda_X\otimes_{\Lambda(*)}P$ with $P$ finitely generated over
the discrete valuation ring or field $\Lambda(*)$. Over such a ring a
finitely generated module has a finite free resolution of length at most
one. Hence $P$ is perfect.

For the direct images we use a compactification to separate the proper
part from the open part. Proper direct image preserves $D^b_{\mathrm{ctf}}(-,\Lambda)$ by
Proposition [proposition-proper-direct-image-constructible-complexes]. Direct image along an open
immersion preserves it by Proposition [proposition-open-direct-image-preserves-finite] for finite $A$ and
Proposition [proposition-direct-image-along-open-immersion] for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$.
If $f=pj$ is a compactification, then $Rf_*=Rp_*Rj_*$ and
$Rf_!=Rp_*j_!$. Each of these composites consists of functors already
known to preserve $D^b_{\mathrm{ctf}}$, which proves both assertions on direct images. That $f^!$
preserves $D^b_{\mathrm{ctf}}(-,\Lambda)$ is part of Theorem [theorem-exceptional-inverse-image].

For internal Hom we reduce to a
first argument supported on a single stratum, where $\cHom$ can be
written in terms of $Ra_*$, $a^!$ and $\otimes^{\mathbf L}$.
The functor $\cHom(-,K)$ sends triangles in the first argument to
triangles, and $D^b_{\mathrm{ctf}}$ is closed under cones and shifts. Hence, for a
triangle $M'\to M\to M''$, the complex $\cHom(M,K)$ lies in $D^b_{\mathrm{ctf}}$
whenever $\cHom(M',K)$ and $\cHom(M'',K)$ do. Using a finite
stratification and finite cones, we may therefore reduce to the case where
the first argument is $a_!P$. Here $a:S\hookrightarrow X$ is locally closed
and $P$ is a locally constant perfect complex on $S$. For finite $A$ this
reduction follows from the bounded flat model and its stupid filtration.
For $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ it follows from the same description of
constructible sheaves on strata. By tensor-Hom adjunction and the
projection formula for $a_!$ we have

$$
\cHom_X(a_!P,K)
\simeq Ra_*\cHom_S(P,a^!K)
\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K).
$$

Here $P^\vee=\cHom_S(P,\Lambda_S)$, and the second identity holds
because $P$ is dualizable. The last term belongs to $D^b_{\mathrm{ctf}}(-,\Lambda)$ by
the cases already established, namely those of $a^!$, of tensor product
and of $Ra_*$.

Finally, since the inclusions are full, the Hom bijections of the ambient
categories restrict to the stated adjunctions.
