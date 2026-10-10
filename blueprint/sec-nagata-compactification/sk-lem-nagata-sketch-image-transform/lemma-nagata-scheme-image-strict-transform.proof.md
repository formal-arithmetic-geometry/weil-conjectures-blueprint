+++
kind  = "proof"
of    = "lemma-nagata-scheme-image-strict-transform"
+++
Put $P=X\times_SY$, $P'=X'\times_SY$, let $W_P\subseteq P$ be the preimage
of $W$, and let $\Omega\subseteq Z\times_PP'$ be the open part lying over
$W_P$. By [def-nagata-strict-transform] the strict transform of $Z$ is the
scheme-theoretic image of $\Omega\hookrightarrow Z\times_PP'$; composing
with the closed immersion $Z\times_PP'\hookrightarrow P'$ (a base change of
$Z\hookrightarrow P$), its ideal sheaf in $P'$ is the kernel of the
composite $j\colon\Omega\to P'$, and the quasi-compactness assumption on
$\Omega\hookrightarrow Z\times_PP'$ makes this kernel describe the
scheme-theoretic image as in [lemma-nagata-scheme-image-ideal-qc].

Since the support of $I$ is disjoint from $U$, we have $U\subseteq W$, so
$h$ lands in $W_P$. By [thm-nagata-global-blowup-complement] the blow-up is
an isomorphism over $W$, hence its base change $\rho$ is an isomorphism over
$W_P$. By [lemma-nagata-strict-transform-over-complement], $\Omega$ is
therefore identified with $Z\times_PW_P$, the open subscheme of $Z$ lying
over $W_P$, compatibly with the projection to $Z$; in particular
$\Omega\to Z$ is an open immersion.

Write $h=\iota_Z\circ\tilde h$ with $\tilde h\colon V\to Z$ the factor map
of [lemma-nagata-scheme-image-ideal-qc]; it is quasi-compact because $h$ is
and $\iota_Z$ is separated. Since $\iota_Z\circ\tilde h=h=\rho\circ h'$, the
pair $(\tilde h,h')$ defines a morphism $k\colon V\to Z\times_PP'$, and $k$
factors through $\Omega$ because $h$ lands in $W_P$; write
$m\colon V\to\Omega$ for the factorization, so that $h'=j\circ m$. Under
$\Omega\cong Z\times_PW_P$ the map $m$ is $\tilde h$ with its target
restricted to the open $Z\times_PW_P$, through which $\tilde h$ factors;
so $m$ is the base change of $\tilde h$ along the open immersion
$Z\times_PW_P\hookrightarrow Z$. As $\tilde h$ is quasi-compact with
scheme-theoretic image $Z$ and open immersions are flat,
[lemma-nagata-dense-flat-pullback] shows that $m$ is quasi-compact with
scheme-theoretic image $\Omega$, i.e. $\mathcal O_\Omega\to m_*\mathcal O_V$
is injective.

Finally, a local section of $\mathcal O_{P'}$ lies in $\ker(h')=\ker(j\circ m)$
if and only if its pullback to $\Omega$ is killed by $m$, if and only if
that pullback is zero, i.e. if and only if it lies in $\ker(j)$. Hence
$\ker(h')=\ker(j)$, which is the asserted equality of the scheme-theoretic
image of $h'$ with the strict transform of $Z$. The lift built from
$\varepsilon^{-1}$ in the statement satisfies $\rho\circ h'=h$, so the
result applies to it.
