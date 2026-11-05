+++
kind = "proof"
of = "theorem-existence-contractible-covers--1"
order = 59002
uses = ["lemma-extremally-disconnected-covers"]
+++
Choose a continuous surjection
$S\to\pi_0(\operatorname{Spec}(R))$ with $S$ compact Hausdorff and
extremally disconnected by Lemma [lemma-extremally-disconnected-covers].
In particular, $S$ is profinite. Form the ring $LC(S,R)$ of locally
constant functions. Its spectrum is $S\times\operatorname{Spec}(R)$.
The closed subset

$$
\{(s,x): s\text{ and }x\text{ have the same image in }
\pi_0(\operatorname{Spec}(R))\}
$$

is a union of connected components. Restrict to this subset by taking
the filtered colimit of the idempotent localizations corresponding to
its clopen neighbourhoods. The resulting $R$-algebra $D$ is ind-Zariski,
and its spectrum is the topological fibre product

$$
|\operatorname{Spec}(D)|
\simeq |\operatorname{Spec}(R)|
\times_{\pi_0(\operatorname{Spec}(R))}S.
$$

This fibre product is w-local, and its closed points are exactly the
inverse image of the closed points of $\operatorname{Spec}(R)$.
An ind-Zariski map identifies local rings. Thus for every maximal ideal
$\mathfrak n$ of $D$, its inverse image $\mathfrak m$ in $R$ is maximal
and $D_{\mathfrak n}\simeq R_{\mathfrak m}$ is strictly henselian.
Hence $D$ is w-strictly local. The projection to $S$ induces a
homeomorphism $\pi_0(\operatorname{Spec}(D))\simeq S$, so $D$ is
w-contractible. Finally, the projection
$\operatorname{Spec}(D)\to\operatorname{Spec}(R)$ is surjective because
$S\to\pi_0(\operatorname{Spec}(R))$ is. Together with flatness of the
ind-Zariski map, this proves faithful flatness.
