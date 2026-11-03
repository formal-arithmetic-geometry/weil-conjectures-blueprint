+++
id = "lem-embedding-extension"
kind = "lemma"
title = "Extension of embeddings and intrinsic weights"
lean = ["PadicAlgCl.exists_ringEquiv_complex_extend", "PadicAlgCl.exists_ringEquiv_complex_apply_eq", "PadicAlgCl.exists_ringHom_complex_apply_eq", "isWeilNumber_algEquiv_apply_iff", "PadicAlgCl.isWeilNumber_of_forall_ringEquiv"]
order = 4378
uses = ["def-weil-algebraic-closure-q", "def-weil-finite-field-fiber", "def-weil-numbers"]
+++
Fix a prime $p$, $a\in\mathbf Z_{\geq1}$, $q=p^a$, $k_0=\Fq$, and
$k=\Fbar$, the fixed algebraic
closure of $k_0$. Fix a prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and
choose an algebraic closure $\overline{\mathbf Q}$ of $\mathbf Q$, and
set

$$
\overline{\mathbf Q}^{(\ell)}=
\{z\in\Qlb:z\text{ is algebraic over }\mathbf Q\}.
$$

An ell-adic realization is an isomorphism
$\jmath:\overline{\mathbf Q}\xrightarrow{\sim}\overline{\mathbf Q}^{(\ell)}$;
this is the algebraic-closure
notion, with the finite-field datum.
Fix $i\in\mathbf Z$, a number field
$L\subset\Qlb$, and a field embedding $\sigma:L\hookrightarrow\mathbf C$.
There is an abstract field isomorphism

$$
\iota:\Qlb\xrightarrow{\sim}\mathbf C
$$

whose restriction to $L$ is $\sigma$. If $\alpha\in\overline{\mathbf Q}$
is such that

$$
|\iota(\jmath(\alpha))|=q^{i/2}
$$

for every ell-adic realization $\jmath$ and every abstract field isomorphism
$\iota:\Qlb\xrightarrow{\sim}\mathbf C$, then

$$
|\tau(\alpha)|=q^{i/2}
$$

for every $\tau:\mathbf Q(\alpha)\hookrightarrow\mathbf C$.
The $q$-Weil-number condition of weight $i$
is stable under
$\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)$.
