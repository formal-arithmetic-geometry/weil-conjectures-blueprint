+++
id = "thm-a1-curve-perverse-heart"
kind = "theorem"
title = "The perverse t-structure on a smooth curve and its heart"
order = 2747
uses = ["cor-pur-adic-and-rational-smooth-dualizing-complexes", "def-per-perverse-subcategories", "def-per-support-condition", "def-weil-t-structure", "def-wf-middle-extension", "lem-exc-closed-support-triangle", "lem-per-dual-lisse-tensor", "lem-weil-closed-costalk-duality", "lem-weil-heart-short-exact-triangles", "prop-constructible-truncations", "prop-sf-localization-all-stages", "prop-weil-heart-abelian", "rem-dl-a1-conventions", "thm-coef-qbar-verdier"]
+++
In the setting of [def-per-support-condition], let the base field $k$ be
perfect (in the applications $k=k_0=\mathbf F_q$ or its algebraic
closure) and let $X=C$ be a smooth separated $k$-scheme of pure dimension
one, for instance $C=A_0$ or a dense open of it. For $k=k_0$ the objects
may equally be Weil complexes on $C_0$, in the conventions of
[rem-dl-a1-conventions]. All conditions below concern cohomology sheaves,
and the operations used in the proof carry the Weil structure, so the
statements hold verbatim in that case. "Sheaf" means a constructible
$\overline{\mathbf Q}_\ell$-sheaf on $C$ (a Weil sheaf in the Weil case),
that is, an object of the heart of the standard t-structure of
[prop-constructible-truncations]. A sheaf is *punctual* if its support is
a finite set of closed points. Let ${}^pD^{\le0}(C)$ and
${}^pD^{\ge0}(C)$ be the classes of [def-per-perverse-subcategories].

1. (*Description.*) For $K\in D^b_c(C,\overline{\mathbf Q}_\ell)$,
   $$
   \begin{aligned}
   K\in{}^pD^{\le0}(C)&\iff \mathcal H^aK=0\ (a>0)\ \text{and}\
   \mathcal H^0K\ \text{is punctual},\\
   K\in{}^pD^{\ge0}(C)&\iff \mathcal H^aK=0\ (a<-1)\ \text{and}\
   \mathcal H^{-1}K\ \text{has no nonzero punctual subsheaf}.
   \end{aligned}
   $$
2. (*t-structure.*) The pair $\bigl({}^pD^{\le0}(C),{}^pD^{\ge0}(C)\bigr)$
   is a bounded t-structure on $D^b_c(C,\overline{\mathbf Q}_\ell)$ in the
   sense of [def-weil-t-structure]. Its heart
   $$
   \mathrm{Perv}(C):={}^pD^{\le0}(C)\cap{}^pD^{\ge0}(C)
   $$
   (the perverse heart candidate of [def-per-perverse-subcategories]) is
   an abelian category.
3. (*The heart.*) $K\in\mathrm{Perv}(C)$ if and only if
   $\mathcal H^aK=0$ for $a\notin\{-1,0\}$, $\mathcal H^0K$ is punctual,
   and $\mathcal H^{-1}K$ has no nonzero punctual subsheaf.
4. (*Basic objects.*) If $j:U\hookrightarrow C$ is a dense open immersion
   and $\mathcal N$ is a lisse sheaf on $U$, then the middle extension
   $(j_*\mathcal N)[1]$ of [def-wf-middle-extension] lies in
   $\mathrm{Perv}(C)$. If $x$ is a closed point with inclusion $i_x$ and
   $E$ is a sheaf on $x$ (a finite-dimensional continuous
   representation of the Galois group, respectively of the Weil group,
   of $k(x)$), then $i_{x*}E$, placed in degree $0$, lies in
   $\mathrm{Perv}(C)$.
5. (*Exact sequences.*) For $P\in\mathrm{Perv}(C)$ the sequence
   $0\to(\mathcal H^{-1}P)[1]\to P\to(\mathcal H^0P)[0]\to0$ is exact in
   $\mathrm{Perv}(C)$. A short exact sequence $0\to Q\to P\to R\to0$ in
   $\mathrm{Perv}(C)$ gives an exact sequence of sheaves
   $$
   0\to\mathcal H^{-1}Q\to\mathcal H^{-1}P\to\mathcal H^{-1}R
   \to\mathcal H^0Q\to\mathcal H^0P\to\mathcal H^0R\to0 .
   $$
