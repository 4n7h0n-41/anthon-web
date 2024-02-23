-- CreateEnum
CREATE TYPE "tax_type" AS ENUM ('INCOME', 'INSURANCE');

-- CreateTable
CREATE TABLE "salaries_log" (
    "id" UUID NOT NULL,
    "month" INTEGER NOT NULL,
    "year" INTEGER NOT NULL,
    "currency" VARCHAR(3) NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "employer" VARCHAR(100) NOT NULL,
    "created_at" DATE NOT NULL DEFAULT CURRENT_DATE,
    "transferred_at" DATE NOT NULL DEFAULT CURRENT_DATE,
    "user_id" UUID NOT NULL,

    CONSTRAINT "salaries_log_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "taxes_log" (
    "id" UUID NOT NULL,
    "month" INTEGER NOT NULL,
    "year" INTEGER NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "created_at" DATE NOT NULL DEFAULT CURRENT_DATE,
    "transferred_at" DATE NOT NULL DEFAULT CURRENT_DATE,
    "tax_type" "tax_type" NOT NULL,
    "user_id" UUID NOT NULL,

    CONSTRAINT "taxes_log_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "users" (
    "id" UUID NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL DEFAULT CURRENT_DATE,
    "updated_at" DATE NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");

-- AddForeignKey
ALTER TABLE "salaries_log" ADD CONSTRAINT "salaries_log_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "taxes_log" ADD CONSTRAINT "taxes_log_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE NO ACTION;
