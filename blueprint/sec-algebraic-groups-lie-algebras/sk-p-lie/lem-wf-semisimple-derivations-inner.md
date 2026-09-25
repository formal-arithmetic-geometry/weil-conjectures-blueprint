+++
id = "lem-wf-semisimple-derivations-inner"
kind = "lemma"
title = "Derivations of a semisimple Lie algebra are inner"
order = 2657
uses = ["def-wf-lie-derivation", "def-wf-semisimple-lie-algebra", "lem-ag-killing-nondegenerate"]
+++
Every derivation of a finite-dimensional semisimple Lie algebra over
$\overline{\mathbf Q}_\ell$ is inner.

## Proof

Let $\mathfrak h$ be semisimple in the sense of
[def-wf-semisimple-lie-algebra]. Its Killing form

$$
B(X,Y)=\operatorname{tr}(\operatorname{ad}(X)\operatorname{ad}(Y))
$$

is nondegenerate by [lem-ag-killing-nondegenerate].

Let $D$ be a derivation as in
[def-wf-lie-derivation]. Nondegeneracy gives a unique
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
