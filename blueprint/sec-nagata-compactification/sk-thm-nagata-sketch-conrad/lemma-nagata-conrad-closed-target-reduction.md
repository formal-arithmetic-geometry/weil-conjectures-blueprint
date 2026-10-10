+++
id = "lemma-nagata-conrad-closed-target-reduction"
kind = "lemma"
title = "Reduction to a closed subscheme of the target"
order = 219
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_partialSection_of_isClosedImmersion"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-global-blowup", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be a scheme with opens $U,V\subseteq X$, let $p\colon Y\to X$ be a
morphism, let $i\colon Y'\hookrightarrow Y$ be a closed immersion and put
$p'=p\circ i$. Let $f'\colon U\to Y'$ be a morphism and
$f=i\circ f'$. Suppose there are a $V$-admissible blow-up
$\pi\colon\widetilde X\to X$, an open $W\subseteq\widetilde X$ containing
$\pi^{-1}(U)$ and a morphism $g\colon W\to Y'$ with $p'\circ g=\pi|_W$ and
$g|_{\pi^{-1}(U)}=f'\circ\pi|_{\pi^{-1}(U)}$, whose graph is closed in
$Y'\times_X\widetilde X$. Then $i\circ g\colon W\to Y$ satisfies
$p\circ i\circ g=\pi|_W$ and $(i\circ g)|_{\pi^{-1}(U)}=f\circ\pi|_{\pi^{-1}(U)}$,
and its graph is closed in $Y\times_X\widetilde X$; that is, the conclusion of
[thm-nagata-conrad-elimination] holds for $(X,U,V,p,f)$ with the same
admissible blow-up and the same open subscheme of it.

## Proof

The extension of $f$ is the extension $g\colon W\to Y'$ of $f'$ followed by
$i$; it is a section of $p$ over $W$ and extends $f$ because $i$ is a
morphism over $X$. The comparison morphism
$Y'\times_XX'\to Y\times_XX'$ is a base change of $i$, hence again a closed
immersion, and the graph of $i\circ g$ is the image of the graph of $g$ under
it. A closed immersion is a closed map, so that image is closed.
