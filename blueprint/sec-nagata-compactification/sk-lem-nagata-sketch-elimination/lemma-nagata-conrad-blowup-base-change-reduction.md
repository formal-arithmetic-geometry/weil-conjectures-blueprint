+++
id = "lemma-nagata-conrad-blowup-base-change-reduction"
kind = "lemma"
title = "Reduction by base change along an admissible blow-up"
order = 322
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_partialSection_of_blowup"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-global-blowup", "prop-nagata-global-blowup-cover-independent"]
+++
Say that data $(X,U,V,p,f)$, consisting of a scheme $X$, opens
$U,V\subseteq X$, a morphism $p\colon Y\to X$ and a section
$f\colon U\to Y$ of $p$ over $U$, *admit an extension* if there are a
$V$-admissible blow-up $\pi\colon\widetilde X\to X$, an open
$W\subseteq\widetilde X$ containing $\pi^{-1}(U)$ and a morphism
$g\colon W\to Y$ with $p\circ g=\pi|_W$ and
$g|_{\pi^{-1}(U)}=f\circ\pi|_{\pi^{-1}(U)}$, whose graph is closed in
$Y\times_X\widetilde X$ (the conclusion of [thm-nagata-conrad-elimination]).

Let $X$ be qcqs, let $U,V\subseteq X$ be open, let $p\colon Y\to X$ be a
morphism and let $f\colon U\to Y$ be a section of $p$ over $U$. Let
$q\colon X'\to X$ be a $V$-admissible blow-up, write $p'\colon Y\times_XX'\to X'$ for the base change of $p$ and $f'\colon q^{-1}(U)\to Y\times_XX'$ for the
base change of $f$. If the data $(X',q^{-1}(U),q^{-1}(V),p',f')$ admit an
extension, then so do $(X,U,V,p,f)$.
