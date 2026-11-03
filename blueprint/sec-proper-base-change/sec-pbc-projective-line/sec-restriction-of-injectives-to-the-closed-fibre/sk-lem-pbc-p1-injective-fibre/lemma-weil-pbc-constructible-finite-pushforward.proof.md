+++
kind  = "proof"
of    = "lemma-weil-pbc-constructible-finite-pushforward"
uses = ["lem-weil-pbc-constructible-finite-pushforward-approximation", "lem-weil-pbc-finite-pushforward-embedding-pullback"]
+++
By Noetherian approximation [lem-weil-pbc-constructible-finite-pushforward-approximation]
there are a morphism $\nu:U\to U'$ to a Noetherian scheme $U'$, a constructible
sheaf of $\Lambda$-modules $C'$ on $U'_{\Et}$ with an isomorphism
$\nu^{-1}C'\cong C$, and a monomorphism

$$
 C'\hookrightarrow\bigoplus_{i=1}^m(h'_i)_*\underline{M_i}
$$

with $h'_i:V'_i\to U'$ finite and locally of finite presentation and $M_i$
finitely generated $\Lambda$-modules. On the Noetherian scheme $U'$ this is
proved by Noetherian induction: on a dense open $V\subseteq U'$ where $C'$ is
finite locally constant, a finite étale cover trivializing $C'|_V$ extends to a
finite morphism $W'\to U'$ (integral closure), whose unit gives a monomorphism
on $V$; on the reduced closed complement one uses the induction hypothesis, and
the two maps together are monic on all geometric stalks.

By [lem-weil-pbc-finite-pushforward-embedding-pullback] the inverse image along
$\nu$ of this monomorphism is again a monomorphism
$\nu^{-1}C'\hookrightarrow\bigoplus_i(h_i)_*\underline{M_i}$ into finite direct
images of the same constant sheaves along finite morphisms $h_i:V_i\to U$
locally of finite presentation (the base changes of the $h'_i$): inverse image
is exact, commutes with finite direct sums and with direct image along finite
morphisms, and preserves constant sheaves. Composing with $C\cong\nu^{-1}C'$
gives the displayed monomorphism. This is the descent argument of Stacks
Project, Lemma 59.74.4 (Tag [09Z7](https://stacks.math.columbia.edu/tag/09Z7)).
