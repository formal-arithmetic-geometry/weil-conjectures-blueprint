+++
kind = "proof"
of = "lemma-descent-finite-coefficient-field--2"
order = 285006
+++
Morphisms descend because $\QbarX$ is the filtered colimit of the $E'_X$
and Hom out of a constructible complex commutes with this colimit
(Lemma [lemma-continuity-ext-out-constructible-complex]). Objects are built from
lisse sheaves by finitely many extensions, each classified by a
morphism, and so they descend as well.

(2) First let $K$ be a constructible $\QbarX$-module, with filtration
$N_1\subset\cdots\subset N_m=K$ as in
Lemma [lemma-constructible-sheaves](3). We descend $N_k$ by induction on
$k$. The subquotient $N_k/N_{k-1}=a_!L$ descends, because $L$ does by
Lemma [lemma-descent-lisse-qbar-sheaves-finite] and $a_!$ commutes with
extension of scalars. Suppose $N_{k-1}$ and
$N_k/N_{k-1}$ descend to $E$. The extension
$0\to N_{k-1}\to N_k\to N_k/N_{k-1}\to0$ gives a distinguished triangle,
classified by a morphism $N_k/N_{k-1}\to N_{k-1}[1]$. By (1) this
morphism descends after a finite extension of $E$. The fibre of the
descended morphism, that is, its cone shifted by $[-1]$, is a model of
$N_k$.

*Source:* the proof of Lemma [lemma-descent-finite-coefficient-field].
