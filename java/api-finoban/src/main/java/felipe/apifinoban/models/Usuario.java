package felipe.apifinoban.models;

import java.util.Date;

public class Usuario {

    private Integer id;
    private String nome;
    private String email;
    private String senha;
    private String cep;
    private String numeroEndereco;
    private Date dataNascimento;

    public Usuario(Integer id, String nome, String email, String senha, String cep, String numeroEndereco, Date dataNascimento) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.cep = cep;
        this.numeroEndereco = numeroEndereco;
        this.dataNascimento = dataNascimento;
    }

    public Integer getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getSenha() {
        return senha;
    }

    public String getCep() {
        return cep;
    }

    public String getNumeroEndereco() {
        return numeroEndereco;
    }

    public Date getDataNascimento() {
        return dataNascimento;
    }
}
