+++
kind  = "proof"
of    = "sk-thm-picard-coherence"
+++
For (b) this is the coherence of higher direct images for proper
morphisms over a locally Noetherian base (Stacks
[02O5](https://stacks.math.columbia.edu/tag/02O5)),
proved with the Čech-to-derived machinery
([sk-thm-picard-cech], [sk-lem-picard-cech-computes]) and the
projective-space case [sk-thm-picard-pn]. Over a Noetherian affine
base, the flatness of $\cF$ turns the Čech complex of a finite
affine cover into a bounded complex of flat modules with coherent
cohomology computing $H^*(X_{T'},\cF_{T'})$ for every $T'\to T$, hence
into a bounded complex of finite free modules with the same property
(Mumford's complex); the general case of (a) reduces to this by
noetherian approximation of $(f,\cF)$ over affine opens of $T$, which
is possible as $f$ and $\cF$ are of finite presentation and $\cF$ is
flat. The vanishing in (a) follows from that complex $K^\bullet$:
$H^q(X_t,\cF_t)=0$ for $q>\dim X_t$, and the top cohomology of
$K^\bullet$ commutes with base change, so by Nakayama it vanishes near
$t$ and $K^\bullet$ can be shortened, degree by degree. Fibre dimension
is bounded over any affine $U$, $f^{-1}(U)$ being quasi-compact; (c)
follows by covering $T$ with finitely many such $U$. None of the
hypotheses can be dropped: over $T=\Spec(k\oplus V)$, $V$ an
infinite-dimensional square-zero ideal, a line bundle $\cL$ on
$E\times_kT$ ($E$ an elliptic curve) deforming $\cO_E$ in a direction
$0\neq a\in V\cong H^1(E,\cO_E)\otimes_kV$ has $f_*\cL$ the kernel of
$k\oplus V\xrightarrow{a}k\oplus V$, i.e. $V$, which is not finitely
generated; and over $T=\coprod_{n\ge1}\Spec k$ with $X=\coprod_n\PP^n_k$
and $\cF=\cO(-n-1)$ on the $n$-th piece, $R^nf_*\cF\neq0$ for every
$n$, so the vanishing bound is only local on $T$.
