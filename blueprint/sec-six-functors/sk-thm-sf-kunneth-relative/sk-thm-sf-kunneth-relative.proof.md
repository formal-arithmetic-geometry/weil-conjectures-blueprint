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
*(3)* Base change for the Cartesian square ([sk-prop-sf-cbc]) gives
$Rq_!(p^*K)\cong Lg^*Rf_!K$.
*(4)* The projection formula for $g$, with $Rf_!K\in\Dctf(B,\Lambda)$ by
[sk-thm-sf-ctf-stability] (iv), gives
$Rg_!\bigl(L\otimes^LLg^*Rf_!K\bigr)\cong Rg_!L\otimes^LRf_!K$. The
reference to [sk-thm-sf-ctf-stability] is a forward one, but not circular:
its clause (iv) is [sk-lem-sf-open-ctf] for $j_!$ and
[sk-thm-sf-direct-image-tor-amplitude] ([sk-cor-sf-direct-image-ctf] on
the pro-étale site) for the proper part, assembled along a compactification,
and neither these nor anything they depend on uses the present theorem. The
compact-support form on closed subschemes is the case of the morphisms
$Z\to\mathrm{Spec}\,k$, $W\to\mathrm{Spec}\,k$ and the objects $i_Z^*K$,
$i_W^*L$ (pullback preserves $\Dctf$), using
$i_Z^*K\boxtimes i_W^*L=(i_Z\times i_W)^*(K\boxtimes L)$. Coherence:
(iv) holds by construction, since $\alpha_{\mathrm{id},f}$,
$\operatorname{Ex}_!$ of an identity square and $\operatorname{PF}_{\mathrm{id}}$
are identities ([sk-thm-sf-comp-composition], [sk-prop-sf-cbc],
[sk-prop-sf-pf-coherence]) and the two symmetries cancel; (i)–(iii) are
identities between composites of $\alpha$, $\operatorname{Ex}_!$ and
$\operatorname{PF}$ attached to the same pasted Cartesian squares, and follow
from the associativity of the composition law, the pasting compatibility of
$\operatorname{Ex}_!$ ([sk-prop-sf-cbc]), the associativity pentagon of
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
