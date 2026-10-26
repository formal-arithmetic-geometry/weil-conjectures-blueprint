+++
id = "det-sp-unique-right-adjoint"
kind = "lemma"
title = "Right adjoints are unique up to a unique counit-compatible isomorphism"
order = 3009
+++
Let $F:\mathcal C\to\mathcal D$ be a functor with two right adjoints $G,J:\mathcal D\to\mathcal C$,
with counits $\varepsilon^G:FG\to\mathrm{id}$ and $\varepsilon^J:FJ\to\mathrm{id}$. For
$K\in\mathcal D$ let $\gamma(K):GK\to JK$ be the $J$-transpose of
$\varepsilon^G(K):FGK\to K$, i.e. the unique morphism with
$\varepsilon^J(K)\circ F(\gamma(K))=\varepsilon^G(K)$, and let $\delta(K):JK\to GK$
be the $G$-transpose of $\varepsilon^J(K)$. Then $\gamma$ and $\delta$ are natural
transformations, mutually inverse, and $\gamma$ is the only natural
transformation $G\to J$ (indeed the only family of morphisms) compatible with
the counits.
