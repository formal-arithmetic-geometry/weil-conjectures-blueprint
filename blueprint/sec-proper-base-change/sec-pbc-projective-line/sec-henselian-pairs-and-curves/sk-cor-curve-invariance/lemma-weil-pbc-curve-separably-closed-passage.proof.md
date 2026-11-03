+++
kind  = "proof"
of    = "lemma-weil-pbc-curve-separably-closed-passage"
+++
Choose compatible algebraic closures $\bar k\subseteq\bar k'$. Since $k$
and $k'$ are separably closed, by [lem-pc-kbar-pure-insep] $\bar k/k$ and $\bar k'/k'$ are purely
inseparable. Their spectrum maps are universal homeomorphisms ([lem-pc-homeo-pure-insep]); the explicit
site equivalence and covering compatibility give the vertical isomorphisms
in

$$
\begin{CD}
H^q(C,F) @>>> H^q(C_{k'},F|)\\
@V{\sim}VV @VV{\sim}V\\
H^q(C_{\bar k},F|) @>>> H^q(C_{\bar k'},F|).
\end{CD}
$$

The lower arrow is an isomorphism by the algebraically closed case. The
square commutes because each route pulls a representative cocycle through
the same composite field map; identity and composition compatibility of the
site equivalence identify the two pullbacks. The upper arrow is therefore
an isomorphism. In particular spectra of separably closed fields, which are
strictly henselian local schemes, introduce no additional stalk ambiguity.
