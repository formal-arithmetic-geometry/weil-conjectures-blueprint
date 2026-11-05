+++
kind = "proof"
of = "lemma-integral-changes-source-base"
order = 679
uses = ["definition-underived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "lemma-injectivity-base-change-map-degree", "lemma-integral-changes-source-base--1", "lemma-integral-changes-source-base--2"]
+++
Both assertions are [Stacks, [0F04](https://stacks.math.columbia.edu/tag/0F04), [0F05](https://stacks.math.columbia.edu/tag/0F05)]. They use three properties of
direct image along an integral morphism $\pi$: it is exact and
conservative [Stacks, [04C2](https://stacks.math.columbia.edu/tag/04C2)], even if $\pi$ is not surjective, and it
commutes with arbitrary base change [Stacks, [0EYP](https://stacks.math.columbia.edu/tag/0EYP)]. By exactness, the
Leray spectral sequence for a composite with $\pi$ degenerates, which means
that direct images along the composite are computed by applying $\pi_*$
first.

We use the notation $b^q_{h,N}$ and $C(h,N)=\operatorname{coker}b^q_{h,N}$ of
the proof of Lemma [lemma-reduction-field], for a $Y$-scheme $T$, its base
change $g_T:T'=Y'\times_YT\to T$, a qcqs morphism $h:Z\to T$ and a sheaf $N$
of $\mathbf Z/n$-modules on $Z_{\acute{e}t}$. By
Lemma [lemma-injectivity-base-change-map-degree], $b^q_{h,N}$ is
injective, so a failure of base change in degree $q$ means $C(h,N)\neq0$.

For the first assertion, let $f:Z\to T$ and $M$ give a failure, so
$C(f,M)\neq0$, and let $\pi:\widetilde Z\to Z$ be integral and surjective.
We show that $C(f\pi,\pi^{-1}M)\neq0$. Since $\pi$ is surjective, the unit
$M\to\pi_*\pi^{-1}M$ is injective, as one sees on stalks. By the second
assertion of Lemma [lemma-injectivity-base-change-map-degree] it induces
an injection $C(f,M)\hookrightarrow C(f,\pi_*\pi^{-1}M)$, and so
$C(f,\pi_*\pi^{-1}M)\neq0$. It remains to identify $C(f,\pi_*\pi^{-1}M)$ with
$C(f\pi,\pi^{-1}M)$. Let $\pi':\widetilde Z_{T'}\to Z_{T'}$ be the base
change of $\pi$, again integral. Upstairs, $\pi_*$ is exact, so the Leray
spectral sequence for $f\circ\pi$ degenerates and gives
$R^qf_*(\pi_*\pi^{-1}M)=R^q(f\pi)_*\pi^{-1}M$. Downstairs, $\pi_*$ commutes
with base change, $g_Z^{-1}\pi_*\pi^{-1}M\simeq\pi'_*g_{\widetilde Z}^{-1}\pi^{-1}M$,
and $\pi'_*$ is exact, so in the same way

$$
R^qf'_*\bigl(g_Z^{-1}\pi_*\pi^{-1}M\bigr)
\simeq R^qf'_*\pi'_*\bigl(g_{\widetilde Z}^{-1}\pi^{-1}M\bigr)
=R^q(f\pi)'_*\bigl(g_{\widetilde Z}^{-1}\pi^{-1}M\bigr).
$$

These identifications are compatible with the base change maps
[Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)], so they carry $b^q_{f,\pi_*\pi^{-1}M}$ to
$b^q_{f\pi,\pi^{-1}M}$. Hence $C(f\pi,\pi^{-1}M)\simeq C(f,\pi_*\pi^{-1}M)\neq0$,
and base change fails for the new source.

For the second assertion, let $f:Z\to T$ factor as $f=\pi\circ f_1$ with
$\pi:T_1\to T$ integral and $f_1:Z\to T_1$, and suppose base change fails
for $f$ and $M$, that is, $C(f,M)\neq0$. We show that it fails for $f_1$ and
$M$ over the new base $T_1$. Put $T'_1=Y'\times_YT_1=T'\times_TT_1$, and let
$\pi':T'_1\to T'$ be the base change of $\pi$, again integral. The base
change map for $f_1$ is

$$
b^q_{f_1,M}:g_{T_1}^{-1}R^qf_{1*}M\longrightarrow R^qf'_{1*}g_Z^{-1}M
\qquad\text{on }T'_{1,\acute{e}t}.
$$

We push it down to $T'$ by $\pi'_*$. Since $\pi'_*$ is exact and
$\pi_*$ commutes with base change,
$\pi'_*g_{T_1}^{-1}R^qf_{1*}M\simeq g_T^{-1}\pi_*R^qf_{1*}M
=g_T^{-1}R^qf_*M$, where the last equality is the degenerate Leray spectral
sequence for $f=\pi f_1$. In the same way
$\pi'_*R^qf'_{1*}g_Z^{-1}M=R^qf'_*g_Z^{-1}M$. Under these identifications
$\pi'_*\bigl(b^q_{f_1,M}\bigr)=b^q_{f,M}$, again because base change maps
compose. Since $\pi'_*$ is exact, it follows that
$\pi'_*C(f_1,M)\simeq C(f,M)\neq0$, so $C(f_1,M)\neq0$, which is the
assertion.
