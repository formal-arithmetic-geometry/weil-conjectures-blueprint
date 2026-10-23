+++
kind = "proof"
of = "lem-weil-pbc-finite-galois-receiving-separable-extensions"
uses = ["def-pc-separably-closed"]
+++
A Galois extension to work in. Let $\Omega$ be a separable closure of $k$: a field extension $\Omega/k$ such that $\Omega$ is separably closed [def-pc-separably-closed] and $\Omega/k$ is separable algebraic. A separable closure is moreover normal over $k$: for every $\alpha\in\Omega$ the minimal polynomial of $\alpha$ over $k$ is a product of polynomials of degree one in $\Omega[T]$. So $\Omega/k$ is Galois (Stacks, Fields, Definition 09I0).

Embedding each $L_i$. For each $i\in\{1,\dots,n\}$ the extension $L_i/k$ is separable algebraic by hypothesis and $\Omega$ is separably closed (step 1), so there is a homomorphism of $k$-algebras $\sigma_i:L_i\to\Omega$ (a separable algebraic extension embeds into any separably closed extension).

A finite Galois subextension containing the images of bases. Since $\dim_kL_i<\infty$, choose a $k$-basis $e_{i1},\dots,e_{id_i}$ of $L_i$ for each $i$, and let $S=\{\sigma_i(e_{ij}):1\le i\le n,\ 1\le j\le d_i\}\subseteq\Omega$, a finite set (empty if $n=0$). Since $\Omega/k$ is Galois (step 1), the Galois closure of $k(S)$ in $\Omega$ is a subfield $L$ with $k\subseteq L\subseteq\Omega$ and $S\subseteq L$ such that $L/k$ is finite ($\dim_kL<\infty$), separable algebraic, and normal (the minimal polynomial over $k$ of every $\beta\in L$ is a product of polynomials of degree one in $L[T]$). Being a subfield of $\Omega$ containing $k$, $L$ is a field extension of $k$.

The maps $\tau_i$. Let $x\in L_i$ and write $x=\sum_jc_je_{ij}$ with $c_j\in k$. Since $\sigma_i$ is $k$-linear, $\sigma_i(x)=\sum_jc_j\sigma_i(e_{ij})$, a $k$-linear combination of elements of $S\subseteq L$; as $L$ is a subfield of $\Omega$ containing $k$, it is closed under such combinations, so $\sigma_i(x)\in L$. Hence $\sigma_i(L_i)\subseteq L$, and $\sigma_i$ with its codomain restricted to $L$ is a homomorphism of $k$-algebras $\tau_i:L_i\to L$ (the operations and the map from $k$ of $L$ are those of $\Omega$). Together with step 3, $L$ and $\tau_1,\dots,\tau_n$ are as claimed. (For $n=0$ the statement asks only for $L$, and step 3 with $S=\emptyset$ gives one, e.g. $L=k$.)
