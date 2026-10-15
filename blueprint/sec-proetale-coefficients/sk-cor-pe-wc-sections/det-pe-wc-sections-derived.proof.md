+++
kind = "proof"
of = "det-pe-wc-sections-derived"
+++
The category of $\mathcal R$-modules is a Grothendieck abelian category, so $K$ has a
K-injective resolution $K\to I$ (Stacks, Tag 079P), and $R\Gamma(U,K)=\Gamma(U,I)$ by
definition. The map $K(U)\to I(U)$ is a quasi-isomorphism: its cone is $\Gamma(U,-)$ of the
cone of $K\to I$, which is acyclic; and an exact functor
([det-pe-wc-sections-exact]) carries acyclic complexes to acyclic complexes, since
acyclicity means exactness of $C^{n-1}\to C^n\to C^{n+1}$ for all $n$ and exact functors
preserve images and kernels. This proves the first assertion. Taking $K=F$ in degree $0$
gives $H^q(U,F)=H^q(F(U)[0])=0$ for $q>0$.
