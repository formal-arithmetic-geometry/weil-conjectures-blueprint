+++
kind  = "proof"
of    = "sk-cor-wrp-rankone-pure"
uses = ["det-p-rankone"]
+++
Put $\varepsilon(w)=\chi(w)c^{-\deg w}$. If $w=gs^d$ with $g\in P$,
then $\varepsilon(w)=\chi(g)$, and hence $\varepsilon$ has finite image
by [sk-p-real-rankone] ([det-p-rankone]). At a closed point $x$ the
eigenvalue is $\varepsilon(F_x)c^{d(x)}$. The first factor has finite
order, hence complex absolute value one ([lem-tw-root-of-unity-modulus]), so
the eigenvalue has absolute value $q_x^{\lambda_\iota(c)/2}$
([cor-wf-rank-one-punctual-purity-curve]). Changing $s$ multiplies $c$ by a
value of $\chi$ on $P$, which has finite order, and so it does not
change this number.
