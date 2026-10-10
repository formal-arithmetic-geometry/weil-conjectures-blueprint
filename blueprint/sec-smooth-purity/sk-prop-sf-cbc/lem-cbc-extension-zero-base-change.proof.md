+++
kind  = "proof"
of    = "lem-cbc-extension-zero-base-change"
+++
Fix a geometric point $\bar x'$ of $X'$ with image
$\bar x=g(\bar x')$. By the stalk characterization of
[def-weil-pbc-extension-by-zero], whose underived form is
[def-weil-pbc-extension-by-zero],

$$
(g^{-1}j_!F)_{\bar x'}=(j_!F)_{\bar x}=
\begin{cases}
F_{\bar x},& \bar x\in U,\\
0,&\bar x\in X\setminus U,
\end{cases}
\qquad
(j'_!g_U^{-1}F)_{\bar x'}=
\begin{cases}
(g_U^{-1}F)_{\bar x'}=F_{\bar x},&\bar x'\in U',\\
0,&\bar x'\in X'\setminus U',
\end{cases}
$$

and $\bar x\in U$ if and only if $\bar x'\in U'$ because the square
is cartesian. Under these identifications the two stalks of the map
agree (the adjoint construction of the map is precisely the
corresponding restriction of sections); the inverse image functors
are exact, and
[lemma-weil-pbc-geometric-stalk-conservative] makes the map an
isomorphism. For complexes the argument applies termwise, exactness
of $j_!$ giving the derived statement.
