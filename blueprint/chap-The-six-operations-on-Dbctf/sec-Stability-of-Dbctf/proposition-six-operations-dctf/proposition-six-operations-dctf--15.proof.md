+++
kind = "proof"
of = "proposition-six-operations-dctf--15"
order = 625031
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-integral-models--3", "lemma-integral-models--4", "lemma-integral-models--5", "proposition-six-operations-dctf--3", "proposition-six-operations-dctf--4", "proposition-six-operations-dctf--5", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1"]
+++
For internal Hom we reduce to a
first argument supported on a single stratum, where $\cHom$ can be
written in terms of $Ra_*$, $a^!$ and $\otimes^{\mathbf L}$.
The functor $\cHom(-,K)$ sends triangles in the first argument to
triangles, and $D^b_{\mathrm{ctf}}$ is closed under cones and shifts. Hence, for a
triangle $M'\to M\to M''$, the complex $\cHom(M,K)$ lies in $D^b_{\mathrm{ctf}}$
whenever $\cHom(M',K)$ and $\cHom(M'',K)$ do. Using a finite
stratification and finite cones, we may therefore reduce to the case where
the first argument is $a_!P$. Here $a:S\hookrightarrow X$ is locally closed
and $P$ is a locally constant perfect complex on $S$. For finite $A$ this
reduction follows from the bounded flat model and its stupid filtration.
For $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ it follows from the same description of
constructible sheaves on strata. By tensor-Hom adjunction and the
projection formula for $a_!$ we have

$$
\cHom_X(a_!P,K)
\simeq Ra_*\cHom_S(P,a^!K)
\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!K).
$$

Here $P^\vee=\cHom_S(P,\Lambda_S)$, and the second identity holds
because $P$ is dualizable. The last term belongs to $D^b_{\mathrm{ctf}}(-,\Lambda)$ by
the cases already established, namely those of $a^!$, of tensor product
and of $Ra_*$.

*Source:* the proof of Proposition [proposition-six-operations-dctf].
