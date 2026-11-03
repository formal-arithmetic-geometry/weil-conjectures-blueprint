+++
kind = "proof"
of = "lem-weil-pbc-etale-generic-irreducible-neighbourhood"
uses = ["pqf-lem-locnoeth-lft"]
+++
*Every generization of $y$ equals $y$.* Let $z\in Y$ with $z\rightsquigarrow y$. Then $f(z)\rightsquigarrow f(y)=\eta$, so $\overline{\{f(z)\}}\supseteq\overline{\{\eta\}}$. Since $\overline{\{\eta\}}$ is an irreducible component, it is a maximal irreducible closed subset, so $\overline{\{f(z)\}}=\overline{\{\eta\}}$, and $f(z)=\eta$ because the underlying space of a scheme is sober (an irreducible closed subset has a unique generic point). Thus $z$ and $y$ lie in the same fibre of $f$. An étale morphism is locally quasi-finite, so its fibres are discrete; a specialization $z\rightsquigarrow y$ between points of a discrete fibre forces $z=y$.

*$y$ lies on exactly one irreducible component of an affine neighbourhood.* $Y$ is locally Noetherian, being locally of finite type over the Noetherian scheme $X$ [pqf-lem-locnoeth-lft]. Choose an affine open $A\subseteq Y$ containing $y$; its coordinate ring is Noetherian, so $A$ is a Noetherian topological space and has finitely many irreducible components. Every irreducible component $Z$ of $A$ containing $y$ has a generic point $z$, which specializes to $y$; by the first step $z=y$, so $Z$ is the closure of $\{y\}$ in $A$. Hence $y$ belongs to exactly one irreducible component of $A$.

*The neighbourhood.* Let $B\subseteq A$ be the complement of the union of the finitely many irreducible components of $A$ not containing $y$. It is open in $A$, contains $y$, and is contained in the remaining component, the closure of $\{y\}$ in $A$. Hence the closure of $\{y\}$ in $B$ is all of $B$. Since $A$ is open in $Y$, $B$ is an open subscheme $W$ of $Y$; it contains $y$, the closure of $\{y\}$ in $W$ is $W$, so $W$ is irreducible with generic point $y$.
