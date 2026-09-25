+++
id = "lem-trf-extension-zero-stalk-traces"
kind = "lemma"
title = "Stalk traces of the Weil extension by zero"
order = 2517
uses = ["def-trf-categorical-trace", "def-trf-frobenius-operators", "def-trf-weil-extension-zero", "def-weil-extension-by-zero", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "fix-lem-finite-tor-perfect", "lem-trf-weil-extension-iterates"]
+++
Use the Weil extension by zero
$(\bar K,\bar\varphi)$ along $j:X\hookrightarrow Y$.
For $m\geq1$ and a
rational point
$y\in Y_0(\mathbf F_{q^m})$, choose its
geometric point
$\bar y$. The local
Frobenius operators satisfy

$$
\operatorname{tr}_A(F_{y,m}\mid\bar K_{\bar y})=
\begin{cases}
\operatorname{tr}_A(F_{y,m}\mid K_{\bar y}),
&y\in X_0(\mathbf F_{q^m}),\\
0,&y\notin X_0(\mathbf F_{q^m}).
\end{cases}
$$

These are categorical traces of
perfect stalk complexes, not assertions about Verdier local terms.

## Proof

The stalk rule in [def-weil-extension-by-zero], applied
degreewise using exactness, gives
$\bar K_{\bar y}=0$ on $Y\setminus X$, and its canonical
identification with $K_{\bar y}$ on $X$. The zero complex has
zero categorical trace by [def-trf-categorical-trace].

On $X$, the iterated Weil structure agrees with the original
one by [lem-trf-weil-extension-iterates]. The transport used
to define $F_{y,m}$ in [def-trf-frobenius-operators]
also restricts to the identical transport on the open site.
Hence the stalk identification intertwines the two operators.
The stalk complexes are perfect by
[fix-lem-finite-tor-perfect], so their traces are defined.
Evaluation and coevaluation are natural under an isomorphism,
giving equality of categorical traces. No identification with a
Verdier local term is invoked.
