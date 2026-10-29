+++
kind  = "proof"
of    = "sk-thm-sf-kunneth-relative"
+++
Four steps, each an instance of one ingredient, and they are the arrows of
the composite.
*(1)* By the composition law, $R(f\times_Bg)_!\cong Rg_!\circ Rq_!$, so
$R(f\times_Bg)_!(K\boxtimes L)\cong Rg_!\bigl(Rq_!(p^*K\otimes^Lq^*L)\bigr)$.
*(2)* The projection formula for $q$ (proved in this section,
[sk-rem-sf-pf-done]) gives
$Rq_!(p^*K\otimes^Lq^*L)\cong Rq_!(p^*K)\otimes^L_\Lambda L$.
*(3)* Base change for the Cartesian square ([det-prop-sf-cbc]) gives
$Rq_!(p^*K)\cong Lg^*Rf_!K$.
*(4)* The projection formula for $g$, with $Rf_!K\in\Dctf(B,\Lambda)$ by
[sk-thm-sf-ctf-stability], gives
$Rg_!\bigl(L\otimes^LLg^*Rf_!K\bigr)\cong Rg_!L\otimes^LRf_!K$. The
reference to [sk-thm-sf-ctf-stability] is a forward one, but not circular:
its $Rf_!$ clause is [sk-lem-sf-open-ctf] for $j_!$ and
[det-thm-sf-direct-image-tor-amplitude] ([sk-cor-sf-direct-image-ctf] on
the pro-étale site) for the proper part, assembled along a compactification,
and neither these nor anything they depend on uses the present theorem. The
compact-support form on closed subschemes is the case of the morphisms
$Z\to\mathrm{Spec}\,k$, $W\to\mathrm{Spec}\,k$ and the objects $i_Z^*K$,
$i_W^*L$ (pullback preserves $\Dctf$), using
$i_Z^*K\boxtimes i_W^*L=(i_Z\times i_W)^*(K\boxtimes L)$. The supported product over a general base $B$ is
$\kappa^{\mathrm{rel}}$ applied to $i_*i^*K$ and $j_*j^*L$ (which lie in
$\Dctf$, since $i^*$ and the exact functor $i_*$ preserve constructibility and
Tor amplitude), using that the exterior product of extensions by zero along
closed immersions is the extension by zero of the exterior product:
$(i_*i^*K)\boxtimes(j_*j^*L)\cong(i\times_Bj)_*(i\times_Bj)^*(K\boxtimes L)$.
Since $i$ and $j$ are proper, $Rf_!i_*=R(fi)_!$ and $Rg_!j_*=R(gj)_!$, so for
$B=\mathrm{Spec}\,k$ this recovers the compact-support form above. Coherence:
(iv) holds by construction, since $\alpha_{\mathrm{id},f}$,
$\operatorname{Ex}_!$ of an identity square and $\operatorname{PF}_{\mathrm{id}}$
are identities ([sk-thm-sf-comp-composition], [det-prop-sf-cbc],
[sk-prop-sf-pf-coherence]) and the two symmetries cancel; (i)–(iii) are
identities between composites of $\alpha$, $\operatorname{Ex}_!$ and
$\operatorname{PF}$ attached to the same pasted Cartesian squares, and follow
from the associativity of the composition law, the pasting compatibility of
$\operatorname{Ex}_!$ ([det-prop-sf-cbc]), the associativity pentagon of
$\operatorname{PF}$ and its compatibility with base change through
$\operatorname{Ex}_!$ (the pentagon and the base-change clause of
[sk-prop-sf-pf-coherence]), the symmetry and associativity of $\otimes^L$,
and the mate identity of [sk-lem-sf-mate]. Explicitly: (iii) is the
base-change clause for $\operatorname{PF}_q$ along the base change of $b$ to
$Y$ and for $\operatorname{PF}_g$ along $b$, combined with the pasting of
$\operatorname{Ex}_!$ for the three squares over $b$; (i) uses the mate
description of $\operatorname{PF}\circ(\operatorname{Ex}_!\otimes1)$ recorded
in the proof of that clause: after reduction to proper $f,g$ (independence of
the compactification), both $\kappa^{\mathrm{rel}}_{K,L}$ and
$\sigma\circ\kappa^{\mathrm{rel}}_{L,K}$ are inverse to the transpose of the
symmetric map $Lp^*Lf^*Rf_*K\otimes^LLq^*Lg^*Rg_*L\to Lp^*K\otimes^LLq^*L$
given by the two counits (lem:sf-kunneth-coherence spells this out).
