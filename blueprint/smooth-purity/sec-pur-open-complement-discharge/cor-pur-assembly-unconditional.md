+++
id = "cor-pur-assembly-unconditional"
kind = "theorem"
title = "The assembly of the purity chapter is unconditional"
order = 3656
tags = ["latex:corollary"]
uses = ["cor-pur-general-admissibility-datum", "cor-sf-ambient-adjoint-discharge", "def-exc-open-complement-bound", "def-pur-conventions", "def-sbc-affine-space", "def-sf-fullcd-used-class", "def-weil-constructible-intervals", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "lem-exc-open-complement-known", "thm-pur-general-admissibility", "thm-pur-open-complement-unconditional"]
+++
In the purity conventions of this chapter
([def-pur-conventions] fixed setting), let $f:X\to Y$ be a
separated finite-type
morphism. Then the hypothesis of [thm-pur-general-admissibility] — the
open-complement condition of [def-exc-open-complement-bound] for the
finitely many chart complements $W_U\subseteq\mathbf A^{d_U}_V$ — holds at
every finite coefficient stage with constants independent of the stage, by
[thm-pur-open-complement-unconditional] and
[lem-exc-open-complement-known]; consequently
[thm-pur-general-admissibility] is a theorem without hypotheses, and with
it [cor-pur-general-admissibility-datum]: $f$ satisfies the two
preservation clauses of [def-weil-exceptional-adjoint-admissibility],
with

$$
D=\max_Ud_U,\qquad
c_U=2(d_U+\dim Y),\qquad
c=\max_U\bigl(c_U+1+2(D-d_U)\bigr)=2D+2\dim Y+1,
$$

so that $Rf^!$ carries $D_c^{[a,b]}(Y,A)$ into
$D_c^{[a-2D,b+2\dim Y+1]}(X,A)$ and finite Tor amplitude in $[a,b]$ to
finite Tor amplitude in $[a-2D,b+2\dim Y+1]$, at every finite coefficient
stage and uniformly in the stage. No restriction to curves, to lisse
coefficients, to constant towers or to smooth morphisms is needed, and the
only hypothesis that the ambient exceptional right adjoint datum contributes
to these two statements is the existence of the right adjoint on the
coefficient class [def-sf-fullcd-used-class], which is the theorem
[cor-sf-ambient-adjoint-discharge].

## Proof

The charts $U\subseteq f^{-1}(V)$ and the integers $d_U$ are those of
[thm-pur-general-admissibility]; each ambient scheme
$\mathbf A^{d_U}_V$ of [def-sbc-affine-space] is of finite type over
$k$ of dimension $d_U+\dim V\leq d_U+\dim Y$, so by
[thm-pur-open-complement-unconditional] with $d=d_U+\dim Y$ the pair
$(W_U,\mathbf A^{d_U}_V)$ satisfies the open-complement condition
[def-exc-open-complement-bound] with the constant
$c_U=2(d_U+\dim Y)$, at every finite coefficient stage at once. That is
exactly the hypothesis of [thm-pur-general-admissibility], so that
theorem applies with these constants; its conclusion is that $f$ satisfies
the two preservation clauses of
[def-weil-exceptional-adjoint-admissibility] with
$c=\max_U(c_U+1+2(D-d_U))$ and $D=\max_Ud_U$, and the identity
$c_U+1+2(D-d_U)=2D+2\dim Y+1$ computed in
[cor-pur-general-admissibility-datum] gives
$c=2D+2\dim Y+1$ and the displayed interval. The assertions about $A$
and about the stage are Step 3 of [thm-pur-open-complement-unconditional]
together with the fact that the charts and their integers do not depend on the
coefficient ring; and the two clauses that
[cor-pur-general-admissibility-datum] quantifies over are the bounded
constructible and finite-Tor objects of
[def-weil-finite-torsion-constructibility] and
[def-weil-finite-tor-amplitude], on which the ambient datum displayed by
[thm-pur-general-admissibility] is the theorem
[cor-sf-ambient-adjoint-discharge] with the class
[def-sf-fullcd-used-class].
