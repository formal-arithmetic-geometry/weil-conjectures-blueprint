+++
kind = "proof"
of = "lemma-descent-finite-coefficient-field--2"
order = 285006
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "lemma-comparison-completed-coefficients--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "lemma-descent-finite-coefficient-field--3", "lemma-descent-finite-coefficient-field--1", "lemma-acyclic-resolutions--1", "proposition-sp-unique-adjoint--1"]
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
