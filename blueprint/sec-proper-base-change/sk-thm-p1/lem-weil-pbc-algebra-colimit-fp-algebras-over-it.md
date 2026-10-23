+++
id = "lem-weil-pbc-algebra-colimit-fp-algebras-over-it"
kind = "lemma"
title = "An algebra is the filtered colimit of the finitely presented algebras mapping to it (Stacks 0BUF)"
lean = ["CommAlgCat.isFiltered_and_isColimit_finitelyPresentedAlgebras"]
order = 1683
+++
Let $R$ be a commutative ring and $\Lambda$ a commutative $R$-algebra. Let $\mathcal P$ be a set of commutative $R$-algebras, each of finite presentation over $R$ (isomorphic as an $R$-algebra to $R[x_1,\dots,x_n]/(f_1,\dots,f_m)$ for some $n,m\ge0$), such that every $R$-algebra of finite presentation is isomorphic as an $R$-algebra to some member of $\mathcal P$ (for example the set of all quotients $R[x_1,\dots,x_n]/I$, $n\ge0$, $I$ a finitely generated ideal, together with any further set of $R$-algebras of finite presentation). Let $\mathcal I$ be the category whose objects are the pairs $(A,\alpha)$ with $A\in\mathcal P$ and $\alpha:A\to\Lambda$ a homomorphism of $R$-algebras, and whose morphisms $(A,\alpha)\to(A',\alpha')$ are the homomorphisms of $R$-algebras $\varphi:A\to A'$ with $\alpha'\circ\varphi=\alpha$. Then $\mathcal I$ is a small filtered category (Stacks, Categories, Definition Tag 002V: $\mathcal I$ has at least one object, any two objects map to a common object, and any two parallel morphisms $\sigma,\tau:x\to y$ are equalized by some $\nu:y\to z$, $\nu\sigma=\nu\tau$), and $(\Lambda,(\alpha)_{(A,\alpha)\in\mathcal I})$ is a colimit of the functor $\mathcal I\to$ (commutative $R$-algebras), $(A,\alpha)\mapsto A$, $\varphi\mapsto\varphi$, in the category of commutative $R$-algebras.
