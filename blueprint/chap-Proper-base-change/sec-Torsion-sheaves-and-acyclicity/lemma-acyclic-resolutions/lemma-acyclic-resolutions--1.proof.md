+++
kind = "proof"
of = "lemma-acyclic-resolutions--1"
order = 346002
uses = []
+++
First let $E^\bullet$ be an exact bounded below complex of
$v$-acyclic objects, and write $Z^m$ for its cycles. The short exact
sequences

$$
0\longrightarrow Z^m\longrightarrow E^m\longrightarrow Z^{m+1}
\longrightarrow 0
$$

and the long exact sequences of right derived functors show inductively
that all $Z^m$ are $v$-acyclic, starting with the zero cycles at the
lower bound. Since $R^1vZ^m=0$, applying $v$ keeps these sequences
short exact. Thus $vE^\bullet$ is exact.

Apply this to the cone of $\varphi$. The cone is exact because
$\varphi$ is a quasi-isomorphism, and it vanishes below $a-1$.
Its term in degree $m$ is $K^{m+1}\oplus L^m$, which is $v$-acyclic
because right derived functors preserve finite direct sums. The image
of the cone under $v$ is therefore exact. Additivity identifies it
with the cone of $v\varphi$, so $v\varphi$ is a quasi-isomorphism.

For $\N$-indexed complexes, extend both complexes and $\varphi$ by
zero to $\mathbb Z$. Extension preserves and reflects
quasi-isomorphisms and commutes with applying $v$, so the first case
gives the assertion.
