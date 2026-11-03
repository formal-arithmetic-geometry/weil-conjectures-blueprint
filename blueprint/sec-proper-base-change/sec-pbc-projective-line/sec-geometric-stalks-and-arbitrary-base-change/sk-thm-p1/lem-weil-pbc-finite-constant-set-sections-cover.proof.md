+++
kind = "proof"
of = "lem-weil-pbc-finite-constant-set-sections-cover"
+++
Since the sheafification map of the constant presheaf is locally surjective, every section $z_i$ has a covering image sieve: the sieve of arrows $g:V\to U$ for which $z_i|_V$ lies in the image of $\eta_V$. A finite intersection of covering sieves is covering, so the intersection $R$ of these finitely many image sieves proves (1).

For (2), let $n,n'\in N$ with $\eta_U(n)=\eta_U(n')$. Since the sheafification map is locally injective, the sieve of arrows $g:V\to U$ on which the restrictions of $n$ and $n'$ in the constant presheaf agree is covering. The restriction maps of the constant presheaf are identities, so if $n\neq n'$ this sieve is the empty sieve, which by hypothesis does not cover $U$. Hence $n=n'$.
