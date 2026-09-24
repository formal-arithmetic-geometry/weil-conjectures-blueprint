+++
id = "lem-wf-semisimple-derivations-inner"
kind = "lemma"
title = "Derivations of a semisimple Lie algebra are inner"
order = 4037
uses = ["def-wf-lie-algebra-derivation", "def-wf-semisimple-lie-algebra", "lem-wf-cartan-trace-criterion"]
+++
Every derivation of a finite-dimensional semisimple Lie algebra over
$\overline{\mathbf Q}_\ell$ is inner.

## Proof

Let $\mathfrak h$ be semisimple in the sense of
[def-wf-semisimple-lie-algebra]. Its Killing form

$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}(X)\operatorname{ad}(Y))
$$

is nondegenerate. To see this without a classification, let
$\mathfrak k=\operatorname{rad}(B)$. Invariance of $B$ makes
$\mathfrak k$ an ideal. Choose a vector-space decomposition
$\mathfrak h=\mathfrak k\oplus L$. If $X\in[\mathfrak k,\mathfrak k]$
and $Y\in\mathfrak k$, then $\operatorname{ad}(X)$ and
$\operatorname{ad}(Y)$ have zero lower-right block on
$\mathfrak h/\mathfrak k$, so

$$
\operatorname{tr}_{\mathfrak k}(\operatorname{ad}(X)|_{\mathfrak k}
\operatorname{ad}(Y)|_{\mathfrak k})=B(X,Y)=0.
$$

The trace criterion [lem-wf-cartan-trace-criterion], applied to
the image of $\mathfrak k$ in $\operatorname{End}(\mathfrak k)$,
shows that this image is solvable. Its kernel is the abelian centre of
$\mathfrak k$, so $\mathfrak k$ is solvable. Since $\mathfrak h$
is semisimple, $\mathfrak k=0$.

Let $D$ be a derivation as in
[def-wf-lie-algebra-derivation]. Nondegeneracy gives a unique
$Z\in\mathfrak h$ such that

$$
B(Z,X)=\operatorname{tr}(D\operatorname{ad}(X))
\qquad(X\in\mathfrak h).
$$

For $X,Y\in\mathfrak h$, the derivation identity gives
$[D,\operatorname{ad}(X)]=\operatorname{ad}(D(X))$. Therefore
cyclicity of trace gives

$$
\begin{aligned}
B(D(X),Y)
&=\operatorname{tr}\bigl([D,\operatorname{ad}(X)]
\operatorname{ad}(Y)\bigr)\\
&=\operatorname{tr}\bigl(D\operatorname{ad}(X)\operatorname{ad}(Y)
-\operatorname{ad}(X)D\operatorname{ad}(Y)\bigr)\\
&=\operatorname{tr}\bigl(D[\operatorname{ad}(X),
\operatorname{ad}(Y)]\bigr)\\
&=B(Z,[X,Y])=B([Z,X],Y).
\end{aligned}
$$

Since
$B$ is nondegenerate, $[Z,X]=D(X)$ for every $X$. Hence
$D=\operatorname{ad}(Z)$, as required.
